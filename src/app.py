from marshmallow.exceptions import ValidationError
from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError
from init import app
from blueprints.cli_bp import db_commands
from blueprints.posts_bp import posts_bp
from blueprints.users_bp import users_bp
from blueprints.comments_bp import comments_bp
from blueprints.tags_bp import tags_bp

app.register_blueprint(db_commands)
app.register_blueprint(posts_bp)
app.register_blueprint(users_bp)
app.register_blueprint(comments_bp)
app.register_blueprint(tags_bp)

@app.route("/")
def index():
    return "MinorNote"

@app.errorhandler(405)
@app.errorhandler(404)
def not_found(err):
    return {'error': 'Not Found'}

@app.errorhandler(ValidationError)
def handle_validation_error(error):
    response = jsonify(error.messages)
    response.status_code = 400
    return response

@app.errorhandler(KeyError)
def missing_key(err):
    return {'error': f'Missing field: {str(err)}'}, 400

@app.errorhandler(SQLAlchemyError)
def handle_sqlalchemy_error(error):
    response = jsonify({"error": "Database error", "message": str(error)})
    response.status_code = 500
    return response

@app.errorhandler(500)
def handle_500_error(error):
    response = jsonify({"error": "Internal Server Error", "message": str(error)})
    response.status_code = 500
    return response

print(app.url_map)
