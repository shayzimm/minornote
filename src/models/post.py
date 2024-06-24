from datetime import date
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text
from init import db, ma

class Post(db.Model):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120))
    content: Mapped[Optional[str]] = mapped_column(Text())
    # user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id'))
    date_created: Mapped[date]

    # user: Mapped['User'] = relationship('User', back_populates='posts')
    # comments: Mapped[List['Comment']] = relationship('Comment', back_populates='post')
    # tags: Mapped[List['Tag']] = relationship('Tag', secondary='post_tags', back_populates='posts')

    # def __repr__(self):
    #     return f'<Post {self.title}>'

class PostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'content', 'date_created')
