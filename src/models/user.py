from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean
from marshmallow import fields, validate
from init import db, ma

# Define the User model with SQLAlchemy ORM
class User(db.Model):
    """
    Represents a User in the database.

    Attributes:
        id (Mapped[int]): The unique identifier for the user.
        username (Mapped[str]): The username of the user.
        email (Mapped[str]): The email address of the user.
        password (Mapped[str]): The password of the user.
        first_name (Mapped[str]): The first name of the user.
        last_name (Mapped[str]): The last name of the user.
        is_admin (Mapped[bool]): A boolean indicating whether the user is an admin.

    Relationships:
        posts (Mapped[List['Post']]): A list of all posts created by the user.
        comments (Mapped[List['Comment']]): A list of all comments made by the user.
    """
    __tablename__ = 'users'

    # Define columns with data types and constraints
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(80), unique=True)
    email: Mapped[str] = mapped_column(String(120), unique=True)
    password: Mapped[str] = mapped_column(String(200))
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    is_admin: Mapped[bool] = mapped_column(Boolean(), server_default='false')

    # Define relationships with other tables
    # A user can create multiple posts
    # This relationship is defined by the posts attribute in the User model
    # uses the relationship function to establish a connection to the Post model
    # The cascade="all, delete-orphan" argument ensures that all associated posts are deleted if the user is deleted
    posts: Mapped[List['Post']] = relationship('Post', back_populates='user', cascade="all, delete-orphan")
    # A user can make multiple comments, defined by the comments attribute in the User model, similar to the posts relationship.
    comments: Mapped[List['Comment']] = relationship('Comment', back_populates='user', cascade="all, delete-orphan")

    # def __repr__(self):
    #     return f'<User {self.username}>'

# Marshmallow schema
# Used to serialize and/or validate SQLAlchemy models
class UserSchema(ma.Schema):
    """
    Marshmallow schema for the User model.

    This schema is used to serialize and/or validate SQLAlchemy models.

    Attributes:
        id (fields.Int): The unique identifier for the user. This field is only included when dumping the schema.
        username (fields.Str): The username of the user. It is required and must be between 1 and 80 characters long.
        email (fields.Email): The email address of the user. It is required.
        password (fields.Str): The password of the user. It is required and must be at least 8 characters long.
        first_name (fields.Str): The first name of the user. It is optional and its length must not exceed 50 characters.
        last_name (fields.Str): The last name of the user. It is optional and its length must not exceed 50 characters.
        is_admin (fields.Bool, dump_only=True): A boolean indicating whether the user is an admin. This field is only included when dumping the schema.

    Class Meta:
        fields: A list of fields that should be included when dumping the schema.
    """
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=1, max=80))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=8))
    first_name = fields.Str(validate=validate.Length(max=50))
    last_name = fields.Str(validate=validate.Length(max=50))
    is_admin = fields.Bool(dump_only=True)

    class Meta:
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_admin')
