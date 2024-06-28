from datetime import date
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from models.comment import Comment, CommentSchema
from auth import admin_or_owner_only, owner_only
from init import db

comments_bp = Blueprint('comments', __name__, url_prefix='/posts')

# Create new comment (C)
@comments_bp.route('/<int:post_id>/comments', methods=['POST'])
@jwt_required()
def create_comment(post_id):
    try:
        comment_info = CommentSchema(only=['content']).load(request.json, unknown='exclude')
    except ValidationError as err:
        return jsonify(err.messages), 400

    comment = Comment(
        content=comment_info.get('content'),
        user_id=get_jwt_identity(),
        post_id=post_id,
        date_created=date.today()
    )
    db.session.add(comment)
    db.session.commit()
    return jsonify(CommentSchema().dump(comment)), 201

# Get all comments on a post (R)
@comments_bp.route('/<int:post_id>/comments', methods=['GET'])
@jwt_required()
def get_comments(post_id):
    comments = Comment.query.filter_by(post_id=post_id).all()
    return jsonify(CommentSchema(many=True).dump(comments)), 200

# Update/edit comment (U)
@comments_bp.route('/<int:post_id>/comments/<int:comment_id>', methods=['PUT', 'PATCH'])
@owner_only
def update_comment(post_id, comment_id):
    comment = db.get_or_404(Comment, comment_id)
    try:
        comment_info = CommentSchema(only=['content']).load(request.json, unknown='exclude')
    except ValidationError as err:
        return jsonify(err.messages), 400

    comment.content = comment_info.get('content', comment.content)
    db.session.commit()
    return jsonify({'message': 'Comment updated successfully'}), 200

# Delete a comment (D)
@comments_bp.route('/<int:post_id>/comments/<int:comment_id>', methods=['DELETE'])
@admin_or_owner_only(Comment, 'comment_id')
def delete_comment(post_id, comment_id):
    comment = db.get_or_404(Comment, comment_id)
    db.session.delete(comment)
    db.session.commit()
    return jsonify({'message': 'Comment deleted successfully'}), 200
