from flask import Blueprint, render_template, url_for, redirect, request, flash, make_response
from flask import session as login_session
from .helpers import get_state, get_random_char
from controllers import CLIENT_SECRET_FILE
from apiclient import discovery
import httplib2
import json
from oauth2client import client


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
        credentials = client.credentials_from_clientsecrets_and_code(CLIENT_SECRET_FILE,
                                                                     ["https://www.googleapis.com/auth/plus.login", 'profile', 'email'],

                                                                     code)
        print(credentials.to_json())
        return "This is just to return"
    else:
        pass