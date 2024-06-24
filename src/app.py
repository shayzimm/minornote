from datetime import timedelta
from flask import request
from flask_jwt_extended import create_access_token
from marshmallow.exceptions import ValidationError
from models.user import User, UserSchema
from models.post import Post, PostSchema
# from models.comment import Comment, CommentSchema
# from models.tag import Tag, TagSchema
from init import db, app, bcrypt
from blueprints.cli_bp import db_commands
from auth import admin_only

app.register_blueprint(db_commands)

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
