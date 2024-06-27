from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.tag import Tag, TagSchema
# from auth import admin_or_owner_only, owner_only
from init import db
from models.post import PostSchema

tags_bp = Blueprint('tags', __name__)

# Retrieve posts by tag (R)
@tags_bp.route('/tags/<int:tag_id>/posts', methods=['GET'])
def get_posts_by_tag(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    posts = tag.posts  # Use the relationship to get all posts associated with the tag
    return jsonify(PostSchema(many=True).dump(posts)), 200

# Create new tag (C)
@tags_bp.route('/tags', methods=['POST'])
@jwt_required()
def create_tag():
    tag_info = TagSchema(only=['name']).load(
        request.json, unknown='exclude'
    )
    tag = Tag(
        name=tag_info.get('name')
    )
    db.session.add(tag)
    db.session.commit()
    return TagSchema().dump(tag), 201

# Get all tags (R)
@tags_bp.route('/tags', methods=['GET'])
def get_tags():
    tags = Tag.query.all()
    return TagSchema(many=True).dump(tags), 200

# Update/edit tag (U)
@tags_bp.route('/tags/<int:tag_id>', methods=['PUT', 'PATCH'])
# @owner_only(Tag, 'tag_id')
def update_tag(tag_id):
    data = request.get_json()
    stmt = db.update(Tag).where(Tag.id == tag_id).values(**data)
    db.session.execute(stmt)
    db.session.commit()
    return {'message': 'Tag updated successfully'}, 200

# Delete a tag (D)
@tags_bp.route('/tags/<int:tag_id>', methods=['DELETE'])
# @admin_or_owner_only(Tag, 'tag_id')
def delete_tag(tag_id):
    stmt = db.delete(Tag).where(Tag.id == tag_id)
    db.session.execute(stmt)
    db.session.commit()
    return {'message': 'Tag deleted successfully'}, 200
