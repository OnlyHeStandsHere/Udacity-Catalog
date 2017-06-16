from models import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    picture = db.Column(db.String(250), nullable=True)

    def __init__(self, user_id, name, email, picture):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.picture = picture

    def __repr__(self):
        return '<User:{}>'.format(self.name)

    @staticmethod
    def create_user(login_session):
        user_id = login_session.get('id')
        name = login_session.get('name')
        email = login_session.get('email')
        picture = login_session.get('picture')
        user = User(user_id, name, email, picture)
        db.session.add(user)
        db.commit()

    @staticmethod
    def check_user_existence(login_session):
        email = login_session.get('email')
        user = db.session.query(db.exists().where(User.email == email)).scalar()
        if user:
            return user
