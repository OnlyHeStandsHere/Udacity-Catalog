from models import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    picture = db.Column(db.String(250), nullable=True)

    def __init__(self, name, email, picture):
        self.name = name
        self.email = email
        self.picture = picture

    def __repr__(self):
        return '<User:{}>'.format(self.name)