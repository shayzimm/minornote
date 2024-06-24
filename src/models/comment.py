from datetime import date
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text
from init import db, ma


class Comment(db.Model):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(Text())
    # user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id'))
    # post_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('posts.id'))
    date_created: Mapped[date]

class CommentSchema(ma.Schema):
    class Meta:
        fields = ("id", "content", "date_created")
