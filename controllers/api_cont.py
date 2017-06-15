from flask import Blueprint, jsonify
from models.restaurants import Restaurant
from models.menu_items import MenuItem

api = Blueprint("api", __name__)


@api.route("/restaurants/json")
def restaurants_json():
    restaurants = Restaurant.query.all()
    return jsonify(restaurants=[r.serialize_menu_items() for r in restaurants])