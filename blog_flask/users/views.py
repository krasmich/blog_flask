from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

users = Blueprint('users', __name__, url_prefix='/users', static_folder='../static')

USERS = {
    1: 'Alice',
    2: 'John',
    3: 'Mike',
}


@users.route('/')
def user_list():
    return render_template(
        'users/list.html',
        users=USERS,
    )


@users.route('/<int:pk>')
def get_user(pk: int):
    try:
        user_name = USERS[pk]
    except KeyError:
        raise NotFound(f'User id {pk} not found')
    return render_template(
        'users/detail.html',
        user_name=user_name,
    )
