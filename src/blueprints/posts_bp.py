from datetime import date
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.post import Post, PostSchema
from auth import admin_only
from init import db

posts_bp = Blueprint('posts', __name__, url_prefix='/posts')

# Get all cards (R)
@posts_bp.route('/')
@admin_only
def all_posts():
    stmt = db.select(Post)
    posts = db.session.scalars(stmt).all()
    return PostSchema(many=True).dump(posts)

# Get one card (R)
@posts_bp.route('/<int:id>')
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
            date_created=date.today()
    )
    db.session.add(post)
    db.session.commit()
    return PostSchema().dump(post), 201

# Update a post (U)
@posts_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_post(id):
    post = db.get_or_404(Post, id)
    post_info = PostSchema(only=['title', 'content']).load(
        request.json, unknown='exclude'
    )
    post.title = post_info.get('title', post.title)
    post.content = post_info.get('content', post.content)
    db.session.commit()
    return PostSchema().dump(post)

# Delete a post (D)
@posts_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_post(id):
    post = db.get_or_404(Post, id)
    db.session.delete(post)
    db.session.commit()
    return {}, 204
