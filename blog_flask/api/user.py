from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog_flask.api.permissions.user import UserListPermission, UserPatchPermission
from blog_flask.config import db
from blog_flask.models import Users
from blog_flask.schemas import UserSchema


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': Users,
        'permission_get': [UserListPermission],
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': Users,
        'permission_patch': [UserPatchPermission],
    }
