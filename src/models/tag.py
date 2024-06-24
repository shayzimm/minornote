from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from init import db, ma

class Tag(db.Model):
    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)

#     posts: Mapped[List['Post']] = relationship('Post', secondary='post_tags', back_populates='tags')

#     def __repr__(self):
#         return f'<Tag {self.name}>'

class TagSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

# Association table for many-to-many relationship between posts and tags
# post_tags = db.Table('post_tags',
#     db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
#     db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
# )