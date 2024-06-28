from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Table, ForeignKey, Integer, Column
from marshmallow import fields, validate
from init import db, ma

# Define the Tag model with SQLAlchemy ORM
class Tag(db.Model):
    """
    Define the Tag model with SQLAlchemy ORM.

    Attributes:
        id (Mapped[int]): Primary key column representing the unique identifier for each tag.
        name (Mapped[str]): Column representing the name of the tag, with a maximum length of 50 characters and uniqueness constraint.
        posts (Mapped[List['Post']]): Relationship attribute representing the many-to-many relationship between tags and posts.

    Methods:
        __init__(self, name: str) -> None: Initialize a new Tag instance with a given name.
    """
    __tablename__ = 'tags'

    # Define columns with data types and constraints
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)

    # Define relationships to other tables
    # A post can have multiple tags, and a tag can be associated with multiple posts
    # This relationship is defined by the tags attribute in the Tag model and the post_tags association table
    posts: Mapped[List['Post']] = relationship('Post', secondary='post_tags', back_populates='tags')

#     def __repr__(self):
#         return f'<Tag {self.name}>'

# Define the Marshmallow schema for Tag
class TagSchema(ma.Schema):
    """
    Define the Marshmallow schema for Tag.

    Attributes:
        id (fields.Int): A field representing the unique identifier for each tag. This field is only included in the serialized output (dump_only=True).
        name (fields.Str): A field representing the name of the tag. This field is required and has a length constraint of 1 to 50 characters.

    Class Meta:
        fields (tuple): A tuple specifying the fields to be included in the serialized output. In this case, it includes 'id' and 'name'.
    """
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=50))

    class Meta:
        fields = ('id', 'name')

# Association table for many-to-many relationship between posts and tags
#
# post_tags: A SQLAlchemy Table object representing the association table for the many-to-many relationship between posts and tags.
#
# Parameters:
#   - 'post_tags' (str): The name of the association table.
#   - 'db.metadata' (SQLAlchemy MetaData object): The metadata object where the association table will be added.
#   - 'post_id' (Column): A SQLAlchemy Column object representing the foreign key to the 'posts' table.
#   - 'tag_id' (Column): A SQLAlchemy Column object representing the foreign key to the 'tags' table.
#
# This association table is used to establish the many-to-many relationship between posts and tags, allowing a post to have multiple tags and a tag to be associated with multiple posts.
post_tags = Table(
    'post_tags',
    db.metadata,
    Column('post_id', Integer, ForeignKey('posts.id', ondelete="CASCADE"), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id', ondelete="CASCADE"), primary_key=True)
)
