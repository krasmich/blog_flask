from flask_login import UserMixin
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash
from sqlalchemy import ForeignKey, func, Column, Integer, DateTime
from datetime import datetime
from blog_flask.database import db


class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(255))

    author = relationship('Author', uselist=False, back_populates='user')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('Users', back_populates='author')
    articles = relationship('Article', back_populates='author')


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, ForeignKey('authors.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False, default="", server_default="")
    text = db.Column(db.Text, nullable=False, default="", server_default="")
    created_at = db.Column(db.DateTime, default=datetime.utcnow, server_default=func.now())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship('Author', back_populates='articles')

