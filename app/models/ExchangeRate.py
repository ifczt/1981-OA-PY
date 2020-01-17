"""
    Created by IFCZT on  2020/1/17 9:00
"""
__author__ = 'IFCZT'

from sqlalchemy import Column, Integer, String, Float,DateTime

from app.models.base import Base


class ExchangeRate(Base):
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    currency_code = Column(String(128), unique=True)
    rate = Column(Float(), unique=True)
    name = Column(String(8), unique=True)
    update_time = Column(DateTime())

    def keys(self):
        return ['name', 'currency_code', 'rate']
