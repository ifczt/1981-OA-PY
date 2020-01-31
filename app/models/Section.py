from app.models.base import Base
from sqlalchemy import Column, Integer, String


class Section(Base):
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(24))

    def keys(self):
        return ['id', 'name']
