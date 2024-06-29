from datetime import timedelta
from flask import request, Blueprint, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from models.user import User, UserSchema
from auth import admin_only, admin_or_owner_only, owner_only, authorize_owner
from init import db, bcrypt

# Initialise the Blueprint for user routes
users_bp = Blueprint('users', __name__, url_prefix='/users')

#  Get all users (R)
# /users/: This endpoint retrieves all users. It requires admin access, which is enforced by the @admin_only decorator.
@users_bp.route('/')
@admin_only
def all_users():
    """
    Retrieve all users in the system.

    This function returns a JSON response containing a list of all users in the system.
    It requires admin privileges to access.

    Parameters:
    None

    Returns:
    A JSON response containing a list of all users in the system, serialized using the UserSchema.
    """
    # Create a SQLAlchemy query to select all users
    # Selects all records from the users table
    # uses the SQLAlchemy ORM to generate the SQL SELECT statement
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    # Serialize the list of users and return as JSON
    return jsonify(UserSchema(many=True).dump(users))

# Get one user (R)
# /users/<int:id>: This endpoint retrieves a specific user by their ID. It requires authentication, enforced by the @jwt_required() decorator.
@users_bp.route('/<int:id>')
@jwt_required()
def one_user(id):
    """
    Retrieve a single user by ID.

    This function returns a JSON response containing a single user with the specified ID.
    It requires a valid JWT token to access.

    Parameters:
    id (int): The ID of the user to retrieve.

    Returns:
    A JSON response containing a single user with the specified ID, serialized using the UserSchema.
    """
    # Retrieve a single user by ID
    # retrieves a single record from the users table by its primary key.
    # If the record is not found, it raises a 404 error.
    user = db.get_or_404(User, id)
    # Serialize the user and return as JSON
    return jsonify(UserSchema().dump(user))

# Login (C)
# /users/login: This endpoint allows a user to log in by providing their email and password. It returns a JWT token if the credentials are valid.
@users_bp.route('/login', methods=['POST'])
def login():
    """
    Authenticate a user and return a JWT token.

    This function validates and deserializes the login credentials provided in the request JSON data.
    If the credentials are valid, it creates a JWT token and returns it in the response.

    Parameters:
    None

    Returns:
    A JSON response containing a JWT token if the login credentials are valid, or an error message if they are not.
    """
    try:
        # Validate and deserialize the request JSON data
        params = UserSchema(only=['email', 'password']).load(request.json, unknown='exclude')
    except ValidationError as err:
        # Return validation errors as JSON with status 400
        return jsonify(err.messages), 400
    
    # Create a SQLAlchemy query to select a user by email
    # Selects a user by their email address
    # The where clause ensures that only the user with the matching email is retrieved
    # Used for login authentication
    stmt = db.select(User).where(User.email == params['email'])
    user = db.session.scalar(stmt)
    # Check if user exists and password matches
    if user and bcrypt.check_password_hash(user.password, params['password']):
        # Create a JWT token and return as JSON
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=2))
        return jsonify({'token': token})
    else:
        # Return an error if email or password is incorrect
        return jsonify({'error': 'Invalid email or password'}), 401
    
# Create new user - Registration (C)
# /users/register: This endpoint allows a new user to register by providing their username, email, password, first name, and last name.
@users_bp.route('/register', methods=['POST'])
def create_user():
    """
    Create a new user and return a JSON response.

    This function validates and deserializes the registration data provided in the request JSON data.
    If the data is valid, it creates a new User instance and adds it to the database.

    Parameters:
    None

    Returns:
    A JSON response containing the newly created user, serialized using the UserSchema, with status 201.
    """
    try:
        # Validate and deserialize the request JSON data
        user_info = UserSchema(only=['username', 'email', 'password', 'first_name', 'last_name']).load(request.json)
    except ValidationError as err:
        # Return validation errors as JSON with status 400
        return jsonify(err.messages), 400
    
    # Check if the username already exists
    if db.session.query(User).filter_by(username=user_info['username']).first():
        return jsonify({'error': 'Username already exists'}), 409
    
    # Create a new User instance
    user = User(
        username=user_info['username'],
        email=user_info['email'],
        password=bcrypt.generate_password_hash(user_info['password']).decode('utf8'),
        first_name=user_info.get('first_name'),
        last_name=user_info.get('last_name'),
        is_admin=user_info.get('is_admin', False)
    )
    
    try:
        # Add the new user to the session and commit to the database
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'A user with the given email already exists'}), 409
    
    # Serialize the new user and return as JSON with status 201
    return jsonify(UserSchema().dump(user)), 201

# Update a user (U)
# /users/<int:id> (PUT/PATCH): This endpoint allows a user to update their information. It requires that the user be the owner of the account, enforced by the @owner_only decorator.
@users_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@owner_only
def update_user(id):
    """
    Update a user's attributes.

    This function retrieves a user by ID and updates their attributes if provided in the request JSON data.
    It requires owner privileges to access.

    Parameters:
    id (int): The ID of the user to update.

    Returns:
    A JSON response containing the updated user, serialized using the UserSchema.
    """
    # Retrieve the user to be updated by ID
    user = db.get_or_404(User, id)
    # Ensure the current user is the owner of the resource
    authorize_owner(user, 'user')
    try:
        # Validate and deserialize the request JSON data
        user_info = UserSchema(only=['username', 'email', 'password', 'first_name', 'last_name']).load(request.json, unknown='exclude')
    except ValidationError as err:
        # Return validation errors as JSON with status 400
        return jsonify(err.messages), 400
    
    # Check if the new username already exists in the database
    existing_user = db.session.query(User).filter(User.username == user_info['username'], User.id != id).first()
    if existing_user:
        return jsonify({'error': 'Username already exists'}), 409
    
    # Update user attributes if provided
    user.username = user_info.get('username', user.username)
    user.email = user_info.get('email', user.email)
    if 'password' in user_info:
        user.password = bcrypt.generate_password_hash(user_info['password']).decode('utf8')
    user.first_name = user_info.get('first_name', user.first_name)
    user.last_name = user_info.get('last_name', user.last_name)
    
    try:
        # Commit the changes to the database
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'An error occurred while updating the user'}), 409
    
    # Serialize the updated user and return as JSON
    return jsonify(UserSchema().dump(user))

# Delete a user (D)
# /users/<int:id> (DELETE): This endpoint allows a user to delete their account. It requires that the user be either the owner or an admin, enforced by the admin_or_owner_only decorator.
@users_bp.route('/<int:id>', methods=['DELETE'])
@admin_or_owner_only(User, 'id', 'user')
def delete_user(id):
    """
    Delete a user from the system.

    This function retrieves a user by ID and deletes them from the database.
    It requires admin or owner privileges to access.

    Parameters:
    id (int): The ID of the user to delete.

    Returns:
    An empty response with status 204.
    """
    # Retrieve the user to be deleted by ID
    user = db.get_or_404(User, id)
    # Ensure the current user is the owner of the resource
    authorize_owner(user, 'user')
    # Delete the user from the database
    db.session.delete(user)
    db.session.commit()
    # Return an empty response with status 204
    return {}, 204
