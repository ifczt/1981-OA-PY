"""
    Created by IFCZT on  2020/1/18 15:04
"""
__author__ = 'IFCZT'

from app.models.base import Base
from sqlalchemy import Column, Integer, String

class Depart(Base):
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128))