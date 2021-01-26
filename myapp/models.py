from flask_login import UserMixin

from myapp.database import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    sub = db.Column(
        db.String(255),
    )
    name = db.Column(
        db.String(255),
    )
    email = db.Column(
        db.String(255),
    )
    profile_pic = db.Column(
        db.String(255),
    )

    def get_id(self):
        return self.id
