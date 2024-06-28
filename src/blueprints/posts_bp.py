from datetime import date
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from models.post import Post, PostSchema
from models.user import User
from auth import admin_or_owner_only
from init import db

# Initialise the Blueprint for post routes
posts_bp = Blueprint('posts', __name__, url_prefix='/posts')

# Get all posts (R)
@posts_bp.route('/', methods=['GET'])
@jwt_required()
def all_posts():
    """
    Get all posts.

    This function retrieves all posts from the database and returns them as JSON.

    Parameters:
    None

    Returns:
    A JSON response containing all posts.
    """
    # Create a SQLAlchemy query to select all posts
    # selects all records from the posts table
    stmt = db.select(Post)
    posts = db.session.scalars(stmt).all()
    # Serialize the list of posts and return as JSON
    return jsonify(PostSchema(many=True).dump(posts))

# Get one post (R)
@posts_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def one_post(id):
    """
    Get one post by ID.

    This function retrieves a single post by its ID from the database and returns it as JSON.

    Parameters:
    id (int): The ID of the post to retrieve.

    Returns:
    A JSON response containing the requested post.
    """
    # Retrieve a single post by ID
    # If the record is not found, it raises a 404 error
    post = db.get_or_404(Post, id)
    # Serialize the post and return as JSON
    return jsonify(PostSchema().dump(post))

# Get all posts by User
@posts_bp.route('/user/<int:user_id>', methods=['GET'])
@jwt_required()
def posts_by_user(user_id):
    """
    Get all posts by a specific user.

    This function retrieves all posts by a specific user from the database and returns them as JSON.

    Parameters:
    user_id (int): The ID of the user whose posts to retrieve.

    Returns:
    A JSON response containing all posts by the specified user.
    """
    # Retrieve all posts by a specific user
    # If the user does not exist, it raises a 404 error
    user = db.get_or_404(User, user_id)
    # Use the relationship to get all posts associated with the user
    posts = user.posts
    # Serialize the list of posts and return as JSON
    return jsonify(PostSchema(many=True).dump(posts))

# Create a new post (C)
@posts_bp.route('/', methods=['POST'])
@jwt_required()
def create_post():
    """
    Create a new post.

    This function creates a new post in the database and returns it as JSON.

    Parameters:
    None

    Returns:
    A JSON response containing the newly created post.
    """
    try:
        # Validate and deserialize the request JSON data
        post_info = PostSchema(only=['title', 'content']).load(request.json, unknown='exclude')
    except ValidationError as err:
        # Return validation errors as JSON with status 400
        return jsonify(err.messages), 400

    # Create a new Post instance
    post = Post(
        title=post_info['title'],
        content=post_info.get('content', ''),
        user_id=get_jwt_identity(),
        date_created=date.today()
    )
    # Add the new post to the session and commit to the database
    db.session.add(post)
    db.session.commit()
    # Serialize the new post and return as JSON with status 201
    return jsonify(PostSchema().dump(post)), 201

# Update a post (U)
@posts_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@admin_or_owner_only(Post, 'id')
def update_post(id):
    """
    Update a post.

    This function updates a post in the database and returns it as JSON.

    Parameters:
    id (int): The ID of the post to update.

    Returns:
    A JSON response containing the updated post.
    """
    # Retrieve the post to be updated by ID
    post = db.get_or_404(Post, id)
    try:
        # Validate and deserialize the request JSON data
        post_info = PostSchema(only=['title', 'content']).load(request.json, unknown='exclude')
    except ValidationError as err:
        # Return validation errors as JSON with status 400
        return jsonify(err.messages), 400

    # Update post attributes if provided
    post.title = post_info.get('title', post.title)
    post.content = post_info.get('content', post.content)
    # Commit the changes to the database
    db.session.commit()
    # Serialize the updated post and return as JSON
    return jsonify(PostSchema().dump(post))

# Delete a post (D)
@posts_bp.route('/<int:id>', methods=['DELETE'])
@admin_or_owner_only(Post, 'id')
def delete_post(id):
    """
    Delete a post.

    This function deletes a post from the database.

    Parameters:
    id (int): The ID of the post to delete.

    Returns:
    An empty response with status 204.
    """
    # Retrieve the post to be deleted by ID
    post = db.get_or_404(Post, id)
    # Delete the post from the database
    db.session.delete(post)
    db.session.commit()
    # Return an empty response with status 204
    return {}, 204
