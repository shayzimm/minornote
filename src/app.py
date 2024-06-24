from datetime import date, timedelta
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Text, Boolean
from typing import Optional
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from marshmallow.exceptions import ValidationError
from functools import wraps
from os import environ

class Base(DeclarativeBase):
    pass

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_KEY')

db = SQLAlchemy(model_class=Base)
db.init_app(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

class User(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(80), unique=True)
    email: Mapped[str] = mapped_column(String(120), unique=True)
    password: Mapped[str] = mapped_column(String(200))
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    is_admin: Mapped[bool] = mapped_column(Boolean(), server_default='false')

# Marshmallow schema
# Used to serialize and/or validate SQLAlchemy models
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_admin')

class Post(db.Model):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120))
    content: Mapped[Optional[str]] = mapped_column(Text())
    # user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id'))
    date_created: Mapped[date]

class PostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'content', 'date_created')

class Comment(db.Model):
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(Text())
    # user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id'))
    # post_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('posts.id'))
    date_created: Mapped[date]

class Tag(db.Model):
    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    
@app.cli.command('db_create')
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

    posts = [
        Post(
            title='testpost',
            content='testcontent',
            date_created=date.today()
        ),
        Post(
            title='testpost2',
            content='testcontent2',
            date_created=date.today()
        ),
        Post(
            title='testpost3',
            content='testcontent3',
            date_created=date.today()
        )
    ]

    comments = [
        Comment(
            content='testcomment',
            date_created=date.today()
        ),
        Comment(
            content='testcomment2',
            date_created=date.today()
        ),
        Comment(
            content='testcomment3',
            date_created=date.today()
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

    db.session.add_all(users)
    db.session.add_all(posts)
    db.session.add_all(comments)
    db.session.add_all(tags)

    db.session.commit()

    print('Users, Posts, Comments, Tags added')

def admin_only(fn):
    @wraps(fn)
    @jwt_required()
    def inner():
        user_id = get_jwt_identity()
        stmt = db.select(User).where(User.id == user_id, User.is_admin)
        user = db.session.scalar(stmt)
        if user:
            return fn()
        else:
            return {'error': 'You must be an admin to access this resource'}, 403
        
    return inner

@app.route('/users')
@admin_only
def all_users():
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    return UserSchema(many=True).dump(users)

@app.route('/users/<int:id>')
def one_user(id):
    user = db.get_or_404(User, id)
    return UserSchema().dump(user)

@app.route('/users/login', methods=['POST'])
def login():
    # email = request.json['email']
    # password = request.json['password']
    params = UserSchema(only=['email', 'password']).load(request.json)
    stmt = db.select(User).where(User.email == params['email'])
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, params['password']):
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=2))
        return {'token': token}
    else:
        return {'error': 'Invalid email or password'}, 401

@app.route('/posts')
@admin_only
def all_posts():
    stmt = db.select(Post)
    posts = db.session.scalars(stmt).all()
    return PostSchema(many=True).dump(posts)

@app.route('/posts/<int:id>')
def one_post(id):
    post = db.get_or_404(Post, id)
    return PostSchema().dump(post)

@app.route("/")
def index():
    return "MinorNote"

@app.errorhandler(405)
@app.errorhandler(404)
def not_found(err):
    return {'error': 'Not Found'}

@app.errorhandler(ValidationError)
def invalid_request(err):
    return {"error": vars(err)['messages']}
