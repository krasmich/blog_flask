from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog_flask.config import db
from blog_flask.models import Author
from blog_flask.schemas import AuthorSchema


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }


class AuthorDetail(ResourceDetail):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }
