from datetime import date
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey
from init import db, ma
from marshmallow import fields
# from models.user import User

class Post(db.Model):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120))
    content: Mapped[Optional[str]] = mapped_column(Text())
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    date_created: Mapped[date]

    user: Mapped['User'] = relationship('User', back_populates='posts')
    # comments: Mapped[List['Comment']] = relationship('Comment', back_populates='post')
    # tags: Mapped[List['Tag']] = relationship('Tag', secondary='post_tags', back_populates='posts')

    # def __repr__(self):
    #     return f'<Post {self.title}>'

class PostSchema(ma.Schema):
    user = fields.Nested('UserSchema', exclude=['password'])
    class Meta:
        fields = ('id', 'title', 'content', 'user', 'date_created')
