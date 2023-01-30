from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog_flask.config import db
from blog_flask.models import Tag
from blog_flask.schemas import TagSchema


class TagList(ResourceList):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag,
    }


class TagDetail(ResourceDetail):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag,
    }
