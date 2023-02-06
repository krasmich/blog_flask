import os

from combojsonapi.event import EventPlugin
from combojsonapi.permission import PermissionPlugin
from combojsonapi.spec import ApiSpecPlugin
from flask import Flask
from flask_migrate import Migrate

from blog_flask.config import admin, db, api

from blog_flask.articles.views import articles
from blog_flask.auth.views import auth, login_manager
from blog_flask.authors.views import authors
from blog_flask.users.views import users


def create_app() -> Flask:
    app = Flask(__name__)
    # postgres://blog_flask_render_user:92RBplLYQmtIZnlskenzVldJYXCeHUt8@dpg-cfgi3ho2i3mg6pdboc3g-a.oregon-postgres.render.com/blog_flask_render

    # SQLAlchemy config
    app.config['SECRET_KEY'] = 'q82&+g0u9%u)g&j_-0p&%*v)wp1&-h9ki1agntbs3vho00o^f0'
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["FLASK_ADMIN_SWATCH"] = 'lux'

    # api config
    app.config["OPENAPI_URL_PREFIX"] = '/api/docs'
    app.config["OPENAPI_VERSION"] = '3.0.0'
    app.config["OPENAPI_SWAGGER_UI_PATH"] = '/'
    app.config["OPENAPI_SWAGGER_UI_VERSION"] = '3.51.1'

    # init apps
    db.init_app(app)
    admin.init_app(app)
    login_manager.init_app(app)

    Migrate(app, db)

    api.plugins = [
        EventPlugin(),
        PermissionPlugin(),
        ApiSpecPlugin(
            app=app,
            tags={
                'Tag': 'Tag API',
                'User': 'User API',
                'Author': 'Author API',
                'Article': 'Article API',
            }
        ),
    ]
    api.init_app(app)

    register_blueprints(app)
    register_api_routes()
    return app


def register_api_routes():
    from blog_flask.api.tag import TagList
    from blog_flask.api.tag import TagDetail
    from blog_flask.api.artical import ArticleList, ArticleDetail
    from blog_flask.api.author import AuthorList, AuthorDetail
    from blog_flask.api.user import UserList, UserDetail

    api.route(TagList, 'tag_list', '/api/tags/', tag='Tag')
    api.route(TagDetail, 'tag_detail', '/api/tags/<int:id>', tag='Tag')

    api.route(UserList, 'user_list', '/api/users/', tag='User')
    api.route(UserDetail, 'user_detail', '/api/users/<int:id>', tag='User')

    api.route(AuthorList, 'author_list', '/api/authors/', tag='Author')
    api.route(AuthorDetail, 'author_detail', '/api/authors/<int:id>', tag='Author')

    api.route(ArticleList, 'article_list', '/api/articles/', tag='Article')
    api.route(ArticleDetail, 'article_detail', '/api/articles/<int:id>', tag='Article')


def register_blueprints(app: Flask):
    from blog_flask import admin

    app.register_blueprint(users)
    app.register_blueprint(articles)
    app.register_blueprint(auth)
    app.register_blueprint(authors)

    admin.register_views()
