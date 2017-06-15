from flask import Blueprint, render_template, url_for, redirect, request, flash, make_response
from flask import session as login_session
from .helpers import get_state
from controllers import CLIENT_SECRET_FILE
import httplib2
import json
from oauth2client import client
import requests


login = Blueprint("login", __name__)


@login.route("/login")
def show_login():
    state = get_state()
    login_session["state"] = state
    return render_template("sessions/login.html", version=get_state(), oauth_state=state)


@login.route("/google_login", methods=['POST'])
def google_login():
    client_state = request.args.get('state')
    if client_state == login_session.get('state'):
        code = request.data

        try:
            credentials = client.credentials_from_clientsecrets_and_code(CLIENT_SECRET_FILE,
                                                                         ["https://www.googleapis.com/auth/plus.login"],
                                                                         code)
        except client.FlowExchangeError:
            response = make_response(json.dumps("Unable to authenticate with Google."), 500)
            response.headers["Content-Type"] = "application/json"
            return response

        login_session['id'] = credentials.id_token["sub"]
        login_session['token'] = credentials.access_token
        login_session['email'] = credentials.id_token['email']
        print(login_session['token'])
        flash("Your are now logged in as {}".format(login_session['email']))
        return url_for('restaurant.index')
    else:
        response = make_response(json.dumps("There was a problem processing your request"), 500)
        response.headers["Content-Type"] = "application/json"
        return response


@login.route("/logout")
def google_logout():
    access_token = login_session.get('token')
    if access_token:
        url = 'https://accounts.google.com/o/oauth2/revoke?token={}'.format(access_token)
        r = requests.get(url)
        if r.ok:
            del login_session['token']
            del login_session['id']
            del login_session['email']
            print("You have been logged out")
            # response = make_response(json.dumps('You Have been successfully logged out.'), 200)
            # response.headers['Content-Type'] = 'application/json'
            # return response
            flash("You Have Been Logged Out!")
            return redirect(url_for("restaurant.index"))
        else:
            response = make_response(json.dumps('Failed to revoke token for given user.'), 400)
            response.headers['Content-Type'] = 'application/json'
            return response
    else:
        response = make_response(json.dumps('The user is not logged in, unable to log out.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response
