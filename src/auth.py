from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import abort, jsonify, make_response
from init import db
from models.user import User

# Route decorator - ensure JWT user is admin
def admin_only(fn):
    @wraps(fn)
    @jwt_required()
    def inner(*args, **kwargs):
        user_id = get_jwt_identity()
        stmt = db.select(User).where(User.id == user_id, User.is_admin)
        user = db.session.scalar(stmt)
        if user:
            return fn(*args, **kwargs)
        else:
            return make_response(jsonify(error='You must be an admin to access this resource'), 403)
        
    return inner

# Route decorator - ensure JWT user is owner of the resource
def owner_only(fn):
    @wraps(fn)
    @jwt_required()
    def inner(*args, **kwargs):
        user_id = get_jwt_identity()
        stmt = db.select(User).where(User.id == user_id)
        user = db.session.scalar(stmt)
        if user:
            return fn(*args, **kwargs)
        else:
            return make_response(jsonify(error='You must be the owner of the resource'), 403)
        
    return inner

# Helper function to authorize the owner of a resource
def authorize_owner(resource):
    user_id = get_jwt_identity()
    if user_id != resource.user_id:
        abort(make_response(jsonify(error='You must be the owner of the resource to access this'), 403))

# Route decorator - ensure JWT user is admin or owner of the resource
def admin_or_owner_only(resource_model, resource_id_param):
    def decorator(fn):
        @wraps(fn)
        @jwt_required()
        def inner(*args, **kwargs):
            user_id = get_jwt_identity()
            resource_id = kwargs.get(resource_id_param)

            # Fetch the resource
            resource = db.session.get(resource_model, resource_id)

            if resource and resource.user_id == user_id:
                return fn(*args, **kwargs)
            else:
                # Check if the user is an admin
                stmt = db.select(User).where(User.id == user_id, User.is_admin)
                user = db.session.scalar(stmt)
                if user:
                    return fn(*args, **kwargs)
                else:
                    return make_response(jsonify(error='You must be the owner of the resource or an admin to access this resource'), 403)
        
        return inner
    return decorator
