from datetime import date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text, ForeignKey
from marshmallow import fields, validate
from init import db, ma

# Define the Comment model with SQLAlchemy ORM
class Comment(db.Model):
    """
    Define the Comment model with SQLAlchemy ORM.
    A comment is associated with a user and a post.

    Attributes:
        id (Mapped[int]): The primary key of the comment.
        content (Mapped[str]): The content of the comment.
        user_id (Mapped[int]): The foreign key referencing the user who created the comment.
        post_id (Mapped[int]): The foreign key referencing the post to which the comment is attached.
        date_created (Mapped[date]): The date when the comment was created.

    Relationships:
        user (Mapped['User']): The user who created the comment.
        post (Mapped['Post']): The post to which the comment is attached.
    """
    __tablename__ = "comments"

    # Define columns with data types and constraints
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(Text())
    # A user can create multiple comments - defined by user_id FK
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"))
    # A post can have multiple comments - defined by post_id FK
    # cascade="all, delete-orphan" argument ensures that all associated comments are deleted if the post is deleted
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id', ondelete="CASCADE"))
    date_created: Mapped[date]

    # Define relationships to other tables
    user: Mapped['User'] = relationship('User', back_populates='comments')
    post: Mapped['Post'] = relationship('Post', back_populates='comments')

    # def __repr__(self):
    #     return f'<Comment {self.content[:20]}>'

# Define the Marshmallow schema for Comment
class CommentSchema(ma.Schema):
    """
    Define the Marshmallow schema for Comment.

    This schema is used to serialize and deserialize Comment objects.

    Attributes:
        id (fields.Int): The primary key of the comment.
        content (fields.Str): The content of the comment.
        user_id (fields.Int): The foreign key referencing the user who created the comment.
        post_id (fields.Int): The foreign key referencing the post to which the comment is attached.
        date_created (fields.DateTime): The date when the comment was created.
        user (fields.Nested('UserSchema', exclude=['password']): The user who created the comment.

    Methods:
        __init__(self, **kwargs): Initializes a new instance of the CommentSchema class.

    Class Meta:
        fields (tuple): A tuple of fields to include in the schema.
    """
    id = fields.Int(dump_only=True)
    content = fields.Str(required=True, validate=validate.Length(min=1))
    user_id = fields.Int(required=True)
    post_id = fields.Int(required=True)
    date_created = fields.DateTime(dump_only=True)
    user = fields.Nested('UserSchema', exclude=['password'])
    
    class Meta:
        fields = ("id", "content", "user_id", "post_id", "user", "date_created")
