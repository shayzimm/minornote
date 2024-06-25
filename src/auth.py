from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import abort, jsonify, make_response
from init import db
from models.user import User

# Route decorator - ensure JWT user is admin
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

# Route decorator - ensure JWT user is owner of the resource
def owner_only(fn):
    @wraps(fn)
    @jwt_required()
    def inner():
        user_id = get_jwt_identity()
        stmt = db.select(User).where(User.id == user_id)
        user = db.session.scalar(stmt)
        if user:
            return fn()
        else:
            return {'error': 'You must be the owner of the resource'}, 403
        
    return inner

def authorize_owner(post):
    user_id = get_jwt_identity()
    if user_id != post.user_id:
        abort(make_response(jsonify(error='You must be the owner of the post to access this resource'), 403))

# Route decorator - ensure JWT user is admin or owner of the resource
def admin_or_owner_only(fn):
    @wraps(fn)
    @jwt_required()
    def inner():
        user_id = get_jwt_identity()
        stmt = db.select(User).where(User.id == user_id)
        user = db.session.scalar(stmt)
        if user:
            return fn()
        else:
            stmt = db.select(User).where(User.id == user_id, User.is_admin)
            user = db.session.scalar(stmt)
            if user:
                return fn()
            else:
                return {'error': 'You must be the owner of the resource or an admin to access this resource'}, 403
        
    return inner
