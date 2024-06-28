from datetime import date
from typing import Optional, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey
from marshmallow import fields, validate
from marshmallow.validate import Length
from init import db, ma

class Post(db.Model):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120))
    content: Mapped[Optional[str]] = mapped_column(Text())
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"))
    date_created: Mapped[date]

    user: Mapped['User'] = relationship('User', back_populates='posts')
    comments: Mapped[List['Comment']] = relationship('Comment', back_populates='post', cascade="all, delete-orphan")
    tags: Mapped[List['Tag']] = relationship('Tag', secondary='post_tags', back_populates='posts')

    # def __repr__(self):
    #     return f'<Post {self.title}>'

class PostSchema(ma.Schema):
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
