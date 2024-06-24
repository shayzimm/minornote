from datetime import timedelta
from flask import request, Blueprint
from flask_jwt_extended import create_access_token
from models.user import User, UserSchema
from auth import admin_only
from init import db, bcrypt

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/')
@admin_only
def all_users():
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    return UserSchema(many=True).dump(users)

@users_bp.route('/<int:id>')
def one_user(id):
    user = db.get_or_404(User, id)
    return UserSchema().dump(user)

@users_bp.route('/login', methods=['POST'])
def login():
    # email = request.json['email']
    # password = request.json['password']
    params = UserSchema(only=['email', 'password']).load(request.json, unknown='exclude')
    stmt = db.select(User).where(User.email == params['email'])
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, params['password']):
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=2))
        return {'token': token}
    else:
        return {'error': 'Invalid email or password'}, 401
    