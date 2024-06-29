from datetime import date
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from models.comment import Comment, CommentSchema
from models.user import User
from auth import admin_or_owner_only, owner_only
from init import db

# Initialise the Blueprint for comment routes
comments_bp = Blueprint('comments', __name__, url_prefix='/posts')

# Create new comment (C)
@comments_bp.route('/<int:post_id>/comments', methods=['POST'])
@jwt_required()
def create_comment(post_id):
    """
    Creates a new comment on a post.
    Requires JWT authentication.

    Args:
        post_id (int): ID of the post to comment on.

    Body (JSON):
        content (str): Content of the comment.

    Returns:
        JSON response containing the created comment.
    """
    try:
        # Validate and deserialize the request JSON data
        comment_info = CommentSchema(only=['content']).load(request.json, unknown='exclude')
    except ValidationError as err:
        # Return validation errors as JSON with status 400
        return jsonify(err.messages), 400

    # Create a new Comment instance
    comment = Comment(
        content=comment_info.get('content'),
        user_id=get_jwt_identity(),
        post_id=post_id,
        date_created=date.today()
    )
    # Add the new comment to the session and commit to the database
    db.session.add(comment)
    db.session.commit()
    # Serialize the new comment and return as JSON with status 201
    return jsonify(CommentSchema().dump(comment)), 201

# Get all comments on a post (R)
@comments_bp.route('/<int:post_id>/comments', methods=['GET'])
@jwt_required()
def get_comments(post_id):
    """
    Retrieves all comments on a specific post.
    Requires JWT authentication.

    Args:
        post_id (int): ID of the post to get comments for.

    Returns:
        JSON response containing all comments on the post.
    """
    # Create a SQLAlchemy query to filter comments by post_id
    comments = Comment.query.filter_by(post_id=post_id).all()
    # Serialize the list of comments and return as JSON
    return jsonify(CommentSchema(many=True).dump(comments)), 200

# Route to get all comments by a specific user (R)
@comments_bp.route('/user/<int:user_id>', methods=['GET'])
@admin_or_owner_only(User, 'user_id')
def comments_by_user(user_id):
    """
    Retrieves all comments by a specific user.
    Requires JWT authentication.

    Args:
        user_id (int): ID of the user to get comments for.

    Returns:
        JSON response containing all comments made by the user.
    """
    # Create a SQLAlchemy query to filter comments by user_id
    comments = Comment.query.filter_by(user_id=user_id).all()
    # Serialize the list of comments and return as JSON
    return jsonify(CommentSchema(many=True).dump(comments)), 200

# Update/edit comment (U)
@comments_bp.route('/<int:post_id>/comments/<int:comment_id>', methods=['PUT', 'PATCH'])
@owner_only
def update_comment(post_id, comment_id):
    """
    Updates an existing comment.
    Requires JWT authentication and that the user is the owner of the comment.

    Args:
        post_id (int): ID of the post the comment belongs to.
        comment_id (int): ID of the comment to update.

    Body (JSON):
        content (str): New content of the comment.

    Returns:
        JSON response with a success message.
    """
    # Retrieve the comment to be updated by ID
    comment = db.get_or_404(Comment, comment_id)
    try:
        # Validate and deserialize the request JSON data
        comment_info = CommentSchema(only=['content']).load(request.json, unknown='exclude')
    except ValidationError as err:
        # Return validation errors as JSON with status 400
        return jsonify(err.messages), 400

    # Update comment attributes if provided
    comment.content = comment_info.get('content', comment.content)
    # Commit the changes to the database
    db.session.commit()
    # Return a success message as JSON
    return jsonify({'message': 'Comment updated successfully'}), 200

# Delete a comment (D)
@comments_bp.route('/<int:post_id>/comments/<int:comment_id>', methods=['DELETE'])
@admin_or_owner_only(Comment, 'comment_id')
def delete_comment(post_id, comment_id):
    """
    Deletes an existing comment.
    Requires JWT authentication and that the user is an admin or the owner of the comment.

    Args:
        post_id (int): ID of the post the comment belongs to.
        comment_id (int): ID of the comment to delete.

    Returns:
        JSON response with a success message.
    """
    # Retrieve the comment to be deleted by ID
    comment = db.get_or_404(Comment, comment_id)
    # Delete the comment from the database
    db.session.delete(comment)
    db.session.commit()
    # Return a success message as JSON
    return jsonify({'message': 'Comment deleted successfully'}), 200
