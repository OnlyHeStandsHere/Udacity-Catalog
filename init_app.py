from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers import restaurant_cont
from models import restaurants, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///restaurants.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.register_blueprint(restaurant_cont.restaurant)
db.app = app
db.init_app(app)