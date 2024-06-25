from datetime import date
from flask import Blueprint
from models.user import User
from models.post import Post
from models.comment import Comment
from models.tag import Tag
from init import db, app, bcrypt

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def db_create():
    db.drop_all()
    db.create_all()
    print('Created tables')

    users = [
        User(
            username='testuser',
            email='testemail@test.com',
            password=bcrypt.generate_password_hash('testpassword').decode('utf8'),
            first_name='testuserfirst',
            last_name='testuserlast',
            is_admin=True
        ),
        User(
            username='testuser2',
            email='testemail2@test.com',
            password=bcrypt.generate_password_hash('testpassword').decode('utf8'),
            first_name='testuserfirst2',
            last_name='testuserlast2',
            is_admin=False
        ),
        User(
            username='testuser3',
            email='testemail3@test.com',
            password=bcrypt.generate_password_hash('testpassword').decode('utf8'),
            first_name='testuserfirst3',
            last_name='testuserlast3',
            is_admin=False
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    posts = [
        Post(
            title='testpost',
            content='testcontent',
            user=users[0],
            date_created=date.today()
        ),
        Post(
            title='testpost2',
            content='testcontent2',
            user=users[1],
            date_created=date.today()
        ),
        Post(
            title='testpost3',
            content='testcontent3',
            user=users[2],
            date_created=date.today()
        )
    ]

    comments = [
        Comment(
            content='testcomment',
            date_created=date.today(), 
            user=users[0],
            post=posts[2]
        ),
        Comment(
            content='testcomment2',
            date_created=date.today(),
            user=users[1],
            post=posts[0]
        ),
        Comment(
            content='testcomment3',
            date_created=date.today(),
            user=users[2],
            post=posts[1]
        )
    ]

    tags = [
        Tag(
            name='testtag'
        ),
        Tag(
            name='testtag2'
        ),
        Tag(
            name='testtag3'
        )
    ]



    db.session.add_all(posts)
    db.session.add_all(comments)
    db.session.add_all(tags)

    db.session.commit()

    print('Users, Posts, Comments, Tags added')
