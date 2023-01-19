from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_user
from werkzeug.exceptions import NotFound
from werkzeug.security import generate_password_hash

from blog_flask.database import db
from blog_flask.forms.user import UserRegisterForm
from blog_flask.models import Users

users = Blueprint('users', __name__, url_prefix='/users', static_folder='../static')


@users.route('register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user.detail', pk=current_user.id))

    form = UserRegisterForm(request.form)
    errors = []
    if request.method == 'POST' and form.validate_on_submit():
        if Users.query.filter_by(email=form.email.data).count():
            form.email.errors.append('email already exists')
            return render_template('users/register.html', form=form)

        _user = Users(
            email=form.email.data,
            name=form.name.data,
            password_hash=generate_password_hash(form.password.data),
        )

        db.session.add(_user)
        db.session.commit()

        login_user(_user)

    return render_template(
        'users/register.html',
        form=form,
        errors=errors,
    )


@users.route('/')
def user_list():
    users = Users.query.all()
    return render_template(
        'users/list.html',
        users=users,
    )


@users.route('/<int:pk>')
def get_user(pk: int):
    user = Users.query.filter_by(id=pk).one_or_none()

    if user is None:
        raise NotFound(f'User #{pk} does not exist!')

    return render_template(
        'users/detail.html',
        user=user
    )
