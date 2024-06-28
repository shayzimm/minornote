from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from models.post import PostSchema
from models.tag import Tag, TagSchema
from auth import admin_only
from init import db

# Initialise the Blueprint for tag routes
tags_bp = Blueprint('tags', __name__)

# Retrieve posts by tag (R)
@tags_bp.route('/tags/<int:tag_id>/posts', methods=['GET'])
@jwt_required()
def get_posts_by_tag(tag_id):
    """
    Retrieves all posts associated with a specific tag.
    Requires JWT authentication.

    Args:
        tag_id (int): ID of the tag to retrieve posts for.

    Returns:
        JSON response containing all posts associated with the tag.
    """
    # Retrieve the tag by ID
    tag = Tag.query.get_or_404(tag_id)
    # This attribute uses the relationship defined in the Tag model to get all posts associated with the tag
    # It leverages the many-to-many relationship between Post and Tag models
    posts = tag.posts  # Use the relationship to get all posts associated with the tag
    # Serialize the list of posts and return as JSON
    return jsonify(PostSchema(many=True).dump(posts)), 200

# Create new tag (C)
@tags_bp.route('/tags', methods=['POST'])
@jwt_required()
def create_tag():
    """
    Creates a new tag.
    Requires JWT authentication.

    Body (JSON):
        name (str): Name of the tag.

    Returns:
        JSON response containing the created tag.
    """
    try:
        # Validate and deserialize the request JSON data
        tag_info = TagSchema(only=['name']).load(request.json, unknown='exclude')
    except ValidationError as err:
        # Return validation errors as JSON with status 400
        return jsonify(err.messages), 400

    # Create a new Tag instance
    tag = Tag(
        name=tag_info.get('name')
    )
    # Add the new tag to the session and commit to the database
    db.session.add(tag)
    db.session.commit()
    # Serialize the new tag and return as JSON with status 201
    return jsonify(TagSchema().dump(tag)), 201

# Get all tags (R)
@tags_bp.route('/tags', methods=['GET'])
@jwt_required()
def get_tags():
    """
    Retrieves all tags.
    Requires JWT authentication.

    Returns:
        JSON response containing all tags.
    """
    # Retrieve all tags from the database
    tags = Tag.query.all()
    # Serialize the list of tags and return as JSON
    return jsonify(TagSchema(many=True).dump(tags)), 200

# Update/edit tag (U)
@tags_bp.route('/tags/<int:tag_id>', methods=['PUT', 'PATCH'])
@admin_only
def update_tag(tag_id):
    """
    Updates an existing tag.
    Requires JWT authentication and that the user is an admin.

    Args:
        tag_id (int): ID of the tag to update.

    Body (JSON):
        name (str): New name of the tag.

    Returns:
        JSON response with a success message.
    """
    # Retrieve the tag to be updated by ID
    tag = db.get_or_404(Tag, tag_id)
    try:
        # Validate and deserialize the request JSON data
        tag_info = TagSchema(only=['name']).load(request.json, unknown='exclude')
    except ValidationError as err:
        # Return validation errors as JSON with status 400
        return jsonify(err.messages), 400

    # Update tag attributes if provided
    tag.name = tag_info.get('name', tag.name)
    # Commit the changes to the database
    db.session.commit()
    # Return a success message as JSON
    return jsonify({'message': 'Tag updated successfully'}), 200

# Delete a tag (D)
@tags_bp.route('/tags/<int:tag_id>', methods=['DELETE'])
@admin_only
def delete_tag(tag_id):
    """
    Deletes an existing tag.
    Requires JWT authentication and that the user is an admin.

    Args:
        tag_id (int): ID of the tag to delete.

    Returns:
        JSON response with a success message.
    """
    # Retrieve the tag to be deleted by ID
    tag = db.get_or_404(Tag, tag_id)
    # Delete the tag from the database
    db.session.delete(tag)
    db.session.commit()
    # Return a success message as JSON
    return jsonify({'message': 'Tag deleted successfully'}), 200
