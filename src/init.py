from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# Define the base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass

# Initialise the Flask application
app = Flask(__name__)

# Configure the application with environment variables
app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY') # Secret key for JWT
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_KEY') # Database URI for SQLAlchemy

# Initialise the SQLAlchemy instance
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Initialise the Marshmallow instance for serialisation and deserialization
ma = Marshmallow(app)

# Initialise Bcrypt instance for password hashing and salting
bcrypt = Bcrypt(app)

# Initialise JWT manager for managing JWT tokens and user authentication
jwt = JWTManager(app)
