from flask import Flask

from blog_flask.articles.views import articles
from blog_flask.users.views import users


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(users)
    app.register_blueprint(articles)
