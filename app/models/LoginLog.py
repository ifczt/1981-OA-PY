"""
    Created by IFCZT on  2020/1/16 13:53
"""
__author__ = 'IFCZT'

from app.models.base import Base
from sqlalchemy import Column, Integer, String

class LoginLog(Base):
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    u_id = Column(String(128))
    ip = Column(String(128))

    def keys(self):
        return [ 'ip', 'create_time']