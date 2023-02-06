import os

from flask_combo_jsonapi import Api
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from blog_flask.admin.views import CustomAdminIndexView

API_URL = os.getenv('API_URL')
db = SQLAlchemy()

admin = Admin(
    index_view=CustomAdminIndexView(),
    name='Blog Admin Panel',
    template_mode='bootstrap4',
)

api = Api()
