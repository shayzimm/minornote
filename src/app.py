from datetime import timedelta
from flask import request
from flask_jwt_extended import create_access_token
from marshmallow.exceptions import ValidationError
from models.user import User, UserSchema
from models.post import Post, PostSchema
# from models.comment import Comment, CommentSchema
# from models.tag import Tag, TagSchema
from init import db, app, bcrypt
from blueprints.cli_bp import db_commands
from blueprints.posts_bp import posts_bp


app.register_blueprint(db_commands)
app.register_blueprint(posts_bp)

@app.route("/")
def index():
    return "MinorNote"

@app.errorhandler(405)
@app.errorhandler(404)
def not_found(err):
    return {'error': 'Not Found'}

@app.errorhandler(ValidationError)
def invalid_request(err):
    return {"error": vars(err)['messages']}

print(app.url_map)
