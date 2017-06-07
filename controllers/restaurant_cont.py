from flask import Blueprint, render_template
from models.restaurants import Restaurant

restaurant = Blueprint('restaurant', __name__)


# make all of our restaurant routes
@restaurant.route('/restaurants/')
def index():
    return render_template("/restaurant/index.html")


@restaurant.route('/restaurant/<int:restaurant_id>/')
def show(restaurant_id):
    return "Here we will show a single restaurant"


@restaurant.route("/restaurant/new/")
def create():
    return "Here we create a new restaurant"


@restaurant.route("/restaurant/<int:restaurant_id>/edit/")
def update(restaurant_id):
    return "Here we will edit a restaurant"


@restaurant.route("/restaurant/<int:restaurant_id>/delete/")
def delete(restaurant_id):
    return "Here we delete a restaurant"