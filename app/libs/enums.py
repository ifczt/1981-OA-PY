"""
    Created by IFCZT on  2020/1/8 16:20
"""
__author__ = 'IFCZT'
from enum import Enum

class AuthorityEnum(Enum):
    SUPER_ADMIN = 1
    ADMIN = 2
    USER = 3

class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201