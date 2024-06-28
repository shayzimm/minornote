from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from models.tag import Tag, TagSchema
from auth import admin_only
from init import db
from models.post import PostSchema

tags_bp = Blueprint('tags', __name__)

# Retrieve posts by tag (R)
@tags_bp.route('/tags/<int:tag_id>/posts', methods=['GET'])
@jwt_required()
def get_posts_by_tag(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    posts = tag.posts  # Use the relationship to get all posts associated with the tag
    return jsonify(PostSchema(many=True).dump(posts)), 200

# Create new tag (C)
@tags_bp.route('/tags', methods=['POST'])
@jwt_required()
def create_tag():
    try:
        tag_info = TagSchema(only=['name']).load(request.json, unknown='exclude')
    except ValidationError as err:
        return jsonify(err.messages), 400

    tag = Tag(
        name=tag_info.get('name')
    )
    db.session.add(tag)
    db.session.commit()
    return jsonify(TagSchema().dump(tag)), 201

# Get all tags (R)
@tags_bp.route('/tags', methods=['GET'])
@jwt_required()
def get_tags():
    tags = Tag.query.all()
    return jsonify(TagSchema(many=True).dump(tags)), 200

# Update/edit tag (U)
@tags_bp.route('/tags/<int:tag_id>', methods=['PUT', 'PATCH'])
@admin_only
def update_tag(tag_id):
    tag = db.get_or_404(Tag, tag_id)
    try:
        tag_info = TagSchema(only=['name']).load(request.json, unknown='exclude')
    except ValidationError as err:
        return jsonify(err.messages), 400

    tag.name = tag_info.get('name', tag.name)
    db.session.commit()
    return jsonify({'message': 'Tag updated successfully'}), 200

# Delete a tag (D)
@tags_bp.route('/tags/<int:tag_id>', methods=['DELETE'])
@admin_only
def delete_tag(tag_id):
    tag = db.get_or_404(Tag, tag_id)
    db.session.delete(tag)
    db.session.commit()
    return jsonify({'message': 'Tag deleted successfully'}), 200
