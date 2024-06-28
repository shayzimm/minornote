from datetime import date
from typing import Optional, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey
from marshmallow import fields, validate
from init import db, ma

# Define the Post model with SQLAlchemy ORM
class Post(db.Model):
    """
    Define the Post model with SQLAlchemy ORM.

    Attributes:
        id (Mapped[int]): Primary key of the post.
        title (Mapped[str]): Title of the post.
        content (Mapped[Optional[str]]): Content of the post.
        user_id (Mapped[int]): Foreign key referencing the user who created the post.
        date_created (Mapped[date]): Date when the post was created.

    Relationships:
        user (Mapped['User']): The user who created the post.
        comments (Mapped[List['Comment']]): A list of comments for the post.
        tags (Mapped[List['Tag']]): A list of tags associated with the post.
    """
    __tablename__ = 'posts'

    # # Define columns with data types and constraints
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120))
    content: Mapped[Optional[str]] = mapped_column(Text())
    # A user can create multiple posts, thanks to the user_id foreign key
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"))
    date_created: Mapped[date]

    # Define relationships to other tables
    user: Mapped['User'] = relationship('User', back_populates='posts')
    # A post can have multiple comments
    comments: Mapped[List['Comment']] = relationship('Comment', back_populates='post', cascade="all, delete-orphan")
    # A post can have multiple tags and a tag can have multiple posts, defined by the tags attribute in Post and the post_tags association
    tags: Mapped[List['Tag']] = relationship('Tag', secondary='post_tags', back_populates='posts')

    # def __repr__(self):
    #     return f'<Post {self.title}>'


# Define the Marshmallow schema for the Post model
# Post model is serialized and deserialized
# It includes validation rules and nested schemas for related models (UserSchema, CommentSchema, and TagSchema)
class PostSchema(ma.Schema):
    """
    Marshmallow schema for the Post model.

    This schema is used to serialize and deserialize the Post model,
    including validation rules and nested schemas for related models (UserSchema, CommentSchema, and TagSchema).

    Attributes:
        id (fields.Int): An integer representing the unique identifier of the post.
        title (fields.Str): A string representing the title of the post. It is required and must be at least 5 characters long.
        content (fields.Str): A string representing the content of the post. It must be at least 1 character long.
        user_id (fields.Int): An integer representing the unique identifier of the user who created the post. It is required.
        date_created (fields.DateTime): A datetime object representing the date when the post was created. It is not included in the serialized output.
        user (fields.Nested): A nested schema representing the user who created the post. It excludes the 'password' field.
        comments (fields.Nested): A nested schema representing a list of comments for the post.
        tags (fields.Nested): A nested schema representing a list of tags associated with the post.

    Class Meta:
        fields: A tuple specifying the fields to be included in the serialized output.
    """
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=5, error="Title must be at least 5 characters"))
    content = fields.Str(validate=validate.Length(min=1))
    user_id = fields.Int(required=True)
    date_created = fields.DateTime(dump_only=True)
    user = fields.Nested('UserSchema', exclude=['password'])
    comments = fields.Nested('CommentSchema', many=True)
    tags = fields.Nested('TagSchema', many=True)

    class Meta:
        fields = ('id', 'title', 'content', 'user_id', 'user', 'comments', 'tags', 'date_created')
