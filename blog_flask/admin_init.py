from flask_admin import Admin

from blog_flask.admin.views import CustomAdminIndexView

admin = Admin(
    index_view=CustomAdminIndexView(),
    name='Blog Admin Panel',
    template_mode='bootstrap4',
)
