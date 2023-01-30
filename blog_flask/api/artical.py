from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog_flask.config import db
from blog_flask.models import Article
from blog_flask.schemas import ArticleSchema


class ArticleList(ResourceList):
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }
