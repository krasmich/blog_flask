import click

from blog_flask.app import create_app
from blog_flask.config import db

app = create_app()


@app.cli.command('init-db')
def init_db():
    """
    Run in your terminal:
    flask init-db
    """

    db.create_all()
    print('done!')


@app.cli.command('create-users')
def create_users():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog_flask.models import Users
    from werkzeug.security import generate_password_hash

    admin = Users(
        email='admin@site.study',
        password_hash=generate_password_hash('admin', method='sha256'),
        name='Администратор')
    user_1 = Users(
        email='denis@site.study',
        password_hash=generate_password_hash('denis', method='sha256'),
        name='Романов Роман Романович')
    user_2 = Users(
        email='kirill@site.study',
        password_hash=generate_password_hash('kirill', method='sha256'),
        name='Семенов Кирилл Андреевич')
    user_3 = Users(
        email='maxim@site.study',
        password_hash=generate_password_hash('maxim', method='sha256'),
        name='Матвеев Максим Филиппович')
    user_4 = Users(
        email='marsel@site.study',
        password_hash=generate_password_hash('marsel', method='sha256'),
        name='Орлов Марсель Максимович')
    user_5 = Users(
        email='kate@site.study',
        password_hash=generate_password_hash('test123'),
        name='Масленникова Екатерина Ивановна')

    db.session.add(admin)
    db.session.add(user_1)
    db.session.add(user_2)
    db.session.add(user_3)
    db.session.add(user_4)
    db.session.add(user_5)
    db.session.commit()

    print('done! created users')


@app.cli.command('create-init-tags')
def create_init_tags():
    """
    Run in your terminal:
    ➜ flask create-tags
    """
    from blog_flask.models import Tag

    with app.app_context():
        tags = ('flask', 'django', 'python', 'gb', 'sqlite')
        for item in tags:
            db.session.add(Tag(name=item))
        db.session.commit()
    click.echo(f'Created tags: {", ".join(tags)}')
