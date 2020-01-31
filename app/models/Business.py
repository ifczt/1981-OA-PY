from app.models.base import Base, db
from sqlalchemy import Column, Integer, String


class Business(Base):
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    u_id = Column(String(128), db.ForeignKey('User.u_id'))
    product = Column(String(64))
    url = Column(String(64))

    def keys(self):
        return ['id', 'product']
