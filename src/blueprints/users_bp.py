from datetime import timedelta
from flask import request, Blueprint, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from models.user import User
from models.user import UserSchema
from auth import admin_only, admin_or_owner_only, owner_only
from init import db, bcrypt
from marshmallow import ValidationError

users_bp = Blueprint('users', __name__, url_prefix='/users')

#  Get all users (R)
@users_bp.route('/')
@admin_only
def all_users():
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    return jsonify(UserSchema(many=True).dump(users))

# Get one user (R)
@users_bp.route('/<int:id>')
@jwt_required()
def one_user(id):
    user = db.get_or_404(User, id)
    return jsonify(UserSchema().dump(user))

# Login (C)
@users_bp.route('/login', methods=['POST'])
def login():
    try:
        params = UserSchema(only=['email', 'password']).load(request.json, unknown='exclude')
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    stmt = db.select(User).where(User.email == params['email'])
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, params['password']):
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=2))
        return jsonify({'token': token})
    else:
        return jsonify({'error': 'Invalid email or password'}), 401
    
# Create new user - Registration (C)
@users_bp.route('/register', methods=['POST'])
def create_user():
    try:
        user_info = UserSchema(only=['username', 'email', 'password', 'first_name', 'last_name']).load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    user = User(
        username=user_info['username'],
        email=user_info['email'],
        password=bcrypt.generate_password_hash(user_info['password']).decode('utf8'),
        first_name=user_info.get('first_name'),
        last_name=user_info.get('last_name'),
        is_admin=user_info.get('is_admin', False)
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(UserSchema().dump(user)), 201

# Update a user (U)
@users_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@owner_only
def update_user(id):
    user = db.get_or_404(User, id)
    try:
        user_info = UserSchema(only=['username', 'email', 'password', 'first_name', 'last_name']).load(request.json, unknown='exclude')
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    user.username = user_info.get('username', user.username)
    user.email = user_info.get('email', user.email)
    if 'password' in user_info:
        user.password = bcrypt.generate_password_hash(user_info['password']).decode('utf8')
    user.first_name = user_info.get('first_name', user.first_name)
    user.last_name = user_info.get('last_name', user.last_name)
    db.session.commit()
    return jsonify(UserSchema().dump(user))

# Delete a user (D)
@users_bp.route('/<int:id>', methods=['DELETE'])
@admin_or_owner_only(User, 'id')
def delete_user(id):
    user = db.get_or_404(User, id)
    db.session.delete(user)
    db.session.commit()
    return {}, 204
