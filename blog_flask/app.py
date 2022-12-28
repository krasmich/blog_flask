from flask import Flask

from blog_flask.articles.views import articles
from blog_flask.auth.views import auth, login_manager
from blog_flask.database import db
from blog_flask.users.views import users


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'q82&+g0u9%u)g&j_-0p&%*v)wp1&-h9ki1agntbs3vho00o^f0'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    login_manager.init_app(app)

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(users)
    app.register_blueprint(articles)
    app.register_blueprint(auth)
