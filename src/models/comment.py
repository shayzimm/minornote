from datetime import date
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text
from init import db, ma

class Comment(db.Model):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(Text())
    # user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id'))
    # post_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('posts.id'))
    date_created: Mapped[date]

    # user: Mapped['User'] = relationship('User', back_populates='comments')
    # post: Mapped['Post'] = relationship('Post', back_populates='comments')

    # def __repr__(self):
    #     return f'<Comment {self.content[:20]}>'

class CommentSchema(ma.Schema):
    class Meta:
        fields = ("id", "content", "date_created")
