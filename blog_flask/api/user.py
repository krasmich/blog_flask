from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog_flask.config import db
from blog_flask.models import Users
from blog_flask.schemas import UserSchema


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': Users,
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': Users,
    }
