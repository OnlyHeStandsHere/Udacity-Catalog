from flask import Blueprint, render_template, url_for, redirect, request, flash
from models.restaurants import Restaurant, db

restaurant = Blueprint('restaurant', __name__)


# make all of our restaurant routes
@restaurant.route('/restaurants/')
def index():
    restaurants = Restaurant.query.all()
    return render_template("restaurant/index.html", restaurants=restaurants)


# creates a new restaurant and serves the form to do so
# upon successful creation redirect to index, otherwise
# flash the error and re-render the form template
@restaurant.route("/restaurant/new/", methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template("restaurant/form.html", restaurant='')
    elif request.method == 'POST':
        rest_name = request.form.get("restaurant_name")
        if rest_name:
            new_restaurant = Restaurant(name=rest_name)
            db.session.add(new_restaurant)
            db.session.commit()
            return redirect(url_for("restaurant.index"))
        else:
            flash("Please enter a valid restaurant name")
            return render_template("restaurant/form.html", restaurant='')
    else:
        flash("Invalid Submission, please try again")
        return render_template("restaurant/form.html", restaurant='')


# Updates the name of an existing restaurant
# if the restaurant cannot be found, we'll flash an error and re-render the form
@restaurant.route("/restaurant/<int:restaurant_id>/edit/", methods=['GET', 'POST'])
def update(restaurant_id):
    current_restaurant = Restaurant.query.get(restaurant_id)
    if current_restaurant:
        if request.method == "GET":
            return render_template("restaurant/form.html", restaurant=current_restaurant)
        elif request.method == "POST":
            name = request.form.get("restaurant_name")
            if name:
                current_restaurant.name = name
                db.session.add(current_restaurant)
                db.session.commit()
                flash("Restaurant has been updated to {}".format(current_restaurant.name))
                return redirect(url_for('restaurant.index'))
        else:
            flash("Invalid Request, please try again")
            return render_template("restaurant/form.html", restaurant='')
    else:
        flash("The restaurant could not be found. Please try again")
        return render_template("restaurant/form.html", restaurant='')


@restaurant.route("/restaurant/<int:restaurant_id>/delete/")
def delete(restaurant_id):
    return "Here we delete a restaurant"