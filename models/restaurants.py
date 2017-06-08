from models import db


class Restaurant(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    menu_items = db.relationship("MenuItem", backref="restaurant")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Restaurant:{}>'.format(self.name)
