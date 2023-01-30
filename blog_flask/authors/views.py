from flask import Blueprint, render_template

from blog_flask.models import Author

authors = Blueprint('authors', __name__, url_prefix='/authors', static_folder='../static')


@authors.route('/')
def author_list():
    authors = Author.query.all()
    return render_template(
        'authors/list.html',
        authors=authors,
    )
