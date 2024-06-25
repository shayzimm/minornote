from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean
from marshmallow import fields
from marshmallow.validate import Length
from init import db, ma

class User(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(80), unique=True)
    email: Mapped[str] = mapped_column(String(120), unique=True)
    password: Mapped[str] = mapped_column(String(200))
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    is_admin: Mapped[bool] = mapped_column(Boolean(), server_default='false')

    posts: Mapped[List['Post']] = relationship('Post', back_populates='user')
    comments: Mapped[List['Comment']] = relationship('Comment', back_populates='user')

    # def __repr__(self):
    #     return f'<User {self.username}>'

# Marshmallow schema
# Used to serialize and/or validate SQLAlchemy models
class UserSchema(ma.Schema):
    email = fields.Email(required=True)
    password = fields.String(validate=Length(min=8), required=True)

    class Meta:
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_admin')