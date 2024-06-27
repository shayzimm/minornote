from datetime import date
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.post import Post, PostSchema
from auth import admin_only, authorize_owner, admin_or_owner_only
from init import db

posts_bp = Blueprint('posts', __name__, url_prefix='/posts')

# Get all posts (R)
@posts_bp.route('/')
@jwt_required()
def all_posts():
    stmt = db.select(Post)
    posts = db.session.scalars(stmt).all()
    return PostSchema(many=True).dump(posts)

# Get one post (R)
@posts_bp.route('/<int:id>')
@jwt_required()
def one_post(id):
    post = db.get_or_404(Post, id)
    return PostSchema().dump(post)

# Create a new post (C)
@posts_bp.route('/', methods=['POST'])
@jwt_required()
def create_post():
    post_info = PostSchema(only=['title', 'content']).load(
        request.json, unknown='exclude'
    )
    post = Post(
            title=post_info['title'],
            content=post_info.get('content', ''),
            user_id=get_jwt_identity(),
            date_created=date.today()
    )
    db.session.add(post)
    db.session.commit()
    return PostSchema().dump(post), 201

# Update a post (U)
@posts_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@admin_or_owner_only(Post, 'id')
def update_post(id):
    post = db.get_or_404(Post, id)
    authorize_owner(post)
    post_info = PostSchema(only=['title', 'content']).load(
        request.json, unknown='exclude'
    )
    post.title = post_info.get('title', post.title)
    post.content = post_info.get('content', post.content)
    db.session.commit()
    return PostSchema().dump(post)

# Delete a post (D)
@posts_bp.route('/<int:id>', methods=['DELETE'])
@admin_or_owner_only(Post, 'id')
def delete_post(id):
    post = db.get_or_404(Post, id)
    db.session.delete(post)
    db.session.commit()
    return {}, 204
