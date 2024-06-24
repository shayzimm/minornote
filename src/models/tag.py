from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from init import db, ma

class Tag(db.Model):
    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)

class TagSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
