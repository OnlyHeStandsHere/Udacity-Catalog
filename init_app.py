from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers import restaurant_cont, menu_item_cont, sessions_cont
from models import restaurants, menu_items, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///restaurants.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.register_blueprint(restaurant_cont.restaurant)
app.register_blueprint(menu_item_cont.menu_items)
app.register_blueprint(sessions_cont.login)
db.app = app
db.init_app(app)