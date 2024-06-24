from datetime import timedelta
from flask import request
from flask_jwt_extended import create_access_token
from models.user import User, UserSchema
from auth import admin_only
from init import app, db, bcrypt

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
    