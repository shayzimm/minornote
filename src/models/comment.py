from datetime import date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text, ForeignKey
from marshmallow import fields, validate
from init import db, ma

class Comment(db.Model):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(Text())
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"))
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id', ondelete="CASCADE"))
    date_created: Mapped[date]

    user: Mapped['User'] = relationship('User', back_populates='comments')
    post: Mapped['Post'] = relationship('Post', back_populates='comments')

    # def __repr__(self):
    #     return f'<Comment {self.content[:20]}>'

class CommentSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    content = fields.Str(required=True, validate=validate.Length(min=1))
    user_id = fields.Int(required=True)
    post_id = fields.Int(required=True)
    date_created = fields.DateTime(dump_only=True)
    user = fields.Nested('UserSchema', exclude=['password'])
    
    class Meta:
        fields = ("id", "content", "user_id", "post_id", "user", "date_created")
