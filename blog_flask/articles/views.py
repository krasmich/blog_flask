from flask import Blueprint, render_template, redirect
from blog_flask.users.views import USERS

articles = Blueprint('articles', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = [
    {
        'id': 1,
        'title': 'Title One',
        'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                'Integer imperdiet imperdiet semper. Sed porta magna vitae elit '
                'accumsan, vel commodo massa porttitor. Aenean suscipit libero quam, '
                'ut vestibulum ex sodales ornare.',
        'author': USERS[1],
    },
    {
        'id': 2,
        'title': 'Title Two',
        'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                'Integer imperdiet imperdiet semper. Sed porta magna vitae elit '
                'accumsan, vel commodo massa porttitor. Aenean suscipit libero quam, '
                'ut vestibulum ex sodales ornare.',
        'author': USERS[2],
    },
    {
        'id': 3,
        'title': 'Title Three',
        'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                'Integer imperdiet imperdiet semper. Sed porta magna vitae elit '
                'accumsan, vel commodo massa porttitor. Aenean suscipit libero quam, '
                'ut vestibulum ex sodales ornare.',
        'author': USERS[3],
    }
]


@articles.route('/')
def articles_list():
    return render_template(
        'articles/list.html',
        articles=ARTICLES
    )


@articles.route('/<int:pk>/')
def articles_info(pk: int):
    article = None
    for value in ARTICLES:
        if value['id'] == pk:
            article = value
            break

    if not article:
        redirect('/articles')

    return render_template(
        'articles/detail.html',
        article=article
    )
