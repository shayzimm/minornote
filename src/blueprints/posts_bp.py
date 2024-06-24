from flask import Blueprint
from models.post import Post, PostSchema
from auth import admin_only
from init import db

posts_bp = Blueprint('posts', __name__, url_prefix='/posts')

@posts_bp.route('/')
@admin_only
def all_posts():
    stmt = db.select(Post)
    posts = db.session.scalars(stmt).all()
    return PostSchema(many=True).dump(posts)

@posts_bp.route('/<int:id>')
def one_post(id):
    post = db.get_or_404(Post, id)
    return PostSchema().dump(post)
