from datetime import date
from flask import Blueprint
from models.user import User
from models.post import Post
from models.comment import Comment
from models.tag import Tag
from init import db, bcrypt

# Initialise the Blueprint for CLI commands
db_commands = Blueprint('db', __name__)

# Command to create and populate the database with sample data
@db_commands.cli.command('create')
def db_create():
    # Drop all existing tables and recreate them
    db.drop_all()
    db.create_all()
    print('Created tables')

    # Create sample users
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

    # Add the users to the session and commit to the database
    db.session.add_all(users)
    db.session.commit()

    # Create sample posts
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

    # Add the posts to the session and commit to the database
    db.session.add_all(posts)
    db.session.commit()

    # Create sample comments
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

    # Add the comments to the session and commit to the database
    db.session.add_all(comments)
    db.session.commit()

    # Create sample tags
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

    # Add the tags to the session and commit to the database
    db.session.add_all(tags)
    db.session.commit()

    # Add relationships between posts and tags
    posts[0].tags.append(tags[0])
    posts[0].tags.append(tags[1])
    posts[1].tags.append(tags[1])
    posts[1].tags.append(tags[2])
    posts[2].tags.append(tags[0])
    posts[2].tags.append(tags[2])

    # Commit the relationships to the database
    db.session.commit()

    print('Users, Posts, Comments, Tags, and relationships added')
