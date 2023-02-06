from typing import Dict

import requests as requests
from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from blog_flask.config import db, API_URL
from blog_flask.forms.article import CreateArticleForm
from blog_flask.models import Article, Author, Tag

articles = Blueprint('articles', __name__, url_prefix='/articles', static_folder='../static')


@articles.route('/', methods=['GET'])
def article_list():
    articles: Article = Article.query.all()
    count_articles: Dict = requests.get(f'{API_URL}/api/articles/event_get_count/').json()
    return render_template(
        'articles/list.html',
        articles=articles,
        count_articles=count_articles['count'],
    )


@articles.route('/<int:article_id>/', methods=['GET'])
def articles_info(article_id):
    _article: Article = Article.query.filter_by(
        id=article_id
    ).options(
        joinedload(Article.tags)
    ).one_or_none()

    if _article is None:
        raise NotFound
    return render_template(
        'articles/detail.html',
        article=_article,
    )


@articles.route('/create/', methods=['GET'])
@login_required
def create_article_form():
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]
    return render_template('articles/create.html', form=form)


@articles.route('/', methods=['POST'])
@login_required
def create_article():
    form = CreateArticleForm(request.form)

    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]

    if form.validate_on_submit():
        _article = Article(title=form.title.data.strip(), text=form.text.data)
        if current_user.author:
            _article.author_id = current_user.author.id
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            _article.author_id = author.id

        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                _article.tags.append(tag)

        db.session.add(_article)
        db.session.commit()

        return redirect(url_for('articles.articles_info', article_id=_article.id))

    return render_template('articles/create.html', form=form)
