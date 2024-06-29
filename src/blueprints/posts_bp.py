from datetime import date
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from models.post import Post, PostSchema
from models.user import User
from auth import admin_or_owner_only, authorize_owner
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
    try:
        # Create a SQLAlchemy query to select all posts
        # selects all records from the posts table
        stmt = db.select(Post)
        posts = db.session.scalars(stmt).all()
        # Serialize the list of posts and return as JSON
        return jsonify(PostSchema(many=True).dump(posts)), 200
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

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
    try:
        # Retrieve a single post by ID
        # If the record is not found, it raises a 404 error
        post = db.get_or_404(Post, id)
        # Serialize the post and return as JSON
        return jsonify(PostSchema().dump(post)), 200
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

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
    try:
        user = db.get_or_404(User, user_id)
        posts = user.posts
        return jsonify(PostSchema(many=True).dump(posts)), 200
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

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
        post_info = PostSchema(only=['title', 'content']).load(request.json, unknown='exclude')
    except ValidationError as err:
        return jsonify(err.messages), 400

    try:
        post = Post(
            title=post_info['title'],
            content=post_info.get('content', ''),
            user_id=get_jwt_identity(),
            date_created=date.today()
        )
        db.session.add(post)
        db.session.commit()
        return jsonify(PostSchema().dump(post)), 201
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Update a post (U)
@posts_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@admin_or_owner_only(Post, 'id', 'post')
def update_post(id):
    """
    Update a post.

    This function updates a post in the database and returns it as JSON.

    Parameters:
    id (int): The ID of the post to update.

    Returns:
    A JSON response containing the updated post.
    """
    try:
        post = db.get_or_404(Post, id)
        authorize_owner(post, 'post')
        post_info = PostSchema(only=['title', 'content']).load(request.json, unknown='exclude')
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

    try:
        post.title = post_info.get('title', post.title)
        post.content = post_info.get('content', post.content)
        db.session.commit()
        return jsonify(PostSchema().dump(post)), 200
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Delete a post (D)
@posts_bp.route('/<int:id>', methods=['DELETE'])
@admin_or_owner_only(Post, 'id', 'post')
def delete_post(id):
    """
    Delete a post.

    This function deletes a post from the database.

    Parameters:
    id (int): The ID of the post to delete.

    Returns:
    An empty response with status 204.
    """
    try:
        post = db.get_or_404(Post, id)
        authorize_owner(post, 'post')
        db.session.delete(post)
        db.session.commit()
        return {}, 204
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500
