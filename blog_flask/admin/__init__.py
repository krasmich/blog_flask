def register_views():
    from blog_flask import models
    from blog_flask.admin.views import TagAdminView, ArticleAdminView, UserAdminView
    from blog_flask.admin_init import admin
    from blog_flask.database import db

    admin.add_view(ArticleAdminView(models.Article, db.session, category='Models'))
    admin.add_view(TagAdminView(models.Tag, db.session, category='Models'))
    admin.add_view(UserAdminView(models.Users, db.session, category='Models'))
