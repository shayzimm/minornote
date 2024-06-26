from marshmallow.exceptions import ValidationError
from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from init import app
from blueprints.cli_bp import db_commands
from blueprints.posts_bp import posts_bp
from blueprints.users_bp import users_bp
from blueprints.comments_bp import comments_bp
from blueprints.tags_bp import tags_bp

# Register Blueprints
app.register_blueprint(db_commands)
app.register_blueprint(posts_bp)
app.register_blueprint(users_bp)
app.register_blueprint(comments_bp)
app.register_blueprint(tags_bp)

# Root endpoint
@app.route("/")
def index():
    """
    Root endpoint of the application.
    Returns a welcome message.
    """
    return "Welcome to MinorNote"

# Error handler for 404 and 405 errors
@app.errorhandler(405)
@app.errorhandler(404)
def not_found(err):
    """
    Handles 404 Not Found and 405 Method Not Allowed errors.
    
    Args:
        err: The error object.
    
    Returns:
        JSON response with an error message.
    """
    return {'error': 'Not Found'}

# Error handler for validation errors from Marshmallow
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    """
    Handles validation errors raised by Marshmallow.
    
    Args:
        error: The ValidationError object.
    
    Returns:
        JSON response with the validation error messages.
    """
    response = jsonify(error.messages)
    response.status_code = 400
    return response

# Error handler for missing fields (KeyError)
@app.errorhandler(KeyError)
def missing_key(err):
    """
    Handles KeyError exceptions, typically for missing fields in the request data.
    
    Args:
        err: The KeyError object.
    
    Returns:
        JSON response with an error message indicating the missing field.
    """
    response = jsonify({"error": f"Missing field: {str(err)}"})
    response.status_code = 400
    return response

# Error handler for integrity errors
@app.errorhandler(IntegrityError)
def handle_integrity_error(error):
    """
    Handles IntegrityError exceptions, typically for database constraints violations.

    Args:
        error: The IntegrityError object.

    Returns:
        JSON response with a database error message.

    Raises:
        None

    Example:
        ```python
        from flask import jsonify
        from sqlalchemy.exc import IntegrityError

        @app.errorhandler(IntegrityError)
        def handle_integrity_error(error):
            response = jsonify({"error": "Database error", "message": str(error)})
            response.status_code = 500
            return response
        ```
    """
    response = jsonify({"error": "Integrity error", "message": str(error)})
    response.status_code = 409
    return response


# Error handler for SQLAlchemy errors
@app.errorhandler(SQLAlchemyError)
def handle_sqlalchemy_error(error):
    """
    Handles SQLAlchemy errors.
    
    Args:
        error: The SQLAlchemyError object.
    
    Returns:
        JSON response with a database error message.
    """
    response = jsonify({"error": "Database error", "message": str(error)})
    response.status_code = 500
    return response

# Error handler for general 500 Internal Server errors
@app.errorhandler(500)
def handle_500_error(error):
    """
    Handles general 500 Internal Server errors.
    
    Args:
        error: The error object.
    
    Returns:
        JSON response with an internal server error message.
    """
    response = jsonify({"error": "Internal Server Error", "message": str(error)})
    response.status_code = 500
    return response

@app.errorhandler(403)
def handle_forbidden_error(error):
    """
    Handles 403 Forbidden errors.

    Args:
        error: The error object.

    Returns:
        JSON response with a forbidden error message.

    Raises:
        None

    Example:
        ```python
        from flask import jsonify
        from flask.views import MethodView

        class ForbiddenErrorHandler(MethodView):
            def get(self, error):
                response = jsonify({"error": "Forbidden", "message": str(error)})
                response.status_code = 403
                return response

        app.add_url_rule('/forbidden', view_func=ForbiddenErrorHandler.as_view('forbidden_error_handler'))
        ```
    """
    response = jsonify({"error": "Forbidden", "message": str(error)})
    response.status_code = 403
    return response

# Print the URL map for debugging purposes
print(app.url_map)
