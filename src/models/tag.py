from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Table, ForeignKey, Integer, Column
from marshmallow import fields, validate
from init import db, ma

class Tag(db.Model):
    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)

    posts: Mapped[List['Post']] = relationship('Post', secondary='post_tags', back_populates='tags')

#     def __repr__(self):
#         return f'<Tag {self.name}>'

class TagSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=50))

    class Meta:
        fields = ('id', 'name')

# Association table for many-to-many relationship between posts and tags
post_tags = Table(
    'post_tags',
    db.metadata,
    Column('post_id', Integer, ForeignKey('posts.id', ondelete="CASCADE"), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id', ondelete="CASCADE"), primary_key=True)
)
