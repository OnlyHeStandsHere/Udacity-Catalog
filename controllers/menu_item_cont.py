from flask import Blueprint, flash, render_template, url_for, request, redirect
from models.menu_items import MenuItem, Restaurant, db

menu_items = Blueprint("menu_item", __name__)


@menu_items.route("/restaurant/<int:restaurant_id>/menu/new", methods=['GET', 'POST'])
def create(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if request.method == 'POST':
        restaurant = Restaurant.query.get(restaurant_id)
        name = request.form.get("name")
        desc = request.form.get("desc")
        price = request.form.get("price")
        menu_item = MenuItem(name=name, desc=desc, price=price, restaurant_id=restaurant.id)
        db.session.add(menu_item)
        db.session.commit()
        flash("Menu item added successfully!")
        return redirect(url_for("restaurant.show_menu", restaurant_id=restaurant.id))
    else:
        return render_template("menu/form.html", menu_item='', restaurant=restaurant)


@menu_items.route("/restaurant/<int:restaurant_id>/menu/<int:menu_item_id>/edit", methods=['GET', 'POST'])
def update(restaurant_id, menu_item_id):
    restaurant = Restaurant.query.get(restaurant_id)
    menu_item = MenuItem.query.get(menu_item_id)
    if menu_item:
        if request.method == 'GET':
            return render_template("menu/form.html", menu_item=menu_item, restaurant=restaurant)
        elif request.method == 'POST':
            menu_item.name = request.form.get("name")
            menu_item.desc = request.form.get("desc")
            menu_item.price = request.form.get("price")
            db.session.add(menu_item)
            db.session.commit()
            flash("Menu item updated successfully!")
            return redirect(url_for("restaurant.show_menu", restaurant_id=menu_item.restaurant.id))
        else:
            flash("Invalid Action, Please try again")
            return redirect(url_for("restaurant.menu", restaurant_id=menu_item.restaurant.id))
    else:
        flash("Item not found, please try again")
        return redirect(url_for("restaurant.index"))
