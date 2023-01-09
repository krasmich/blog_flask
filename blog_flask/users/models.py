from flask_login import UserMixin
from werkzeug.security import check_password_hash

from blog_flask.database import db


class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(255))

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
