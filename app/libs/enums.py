"""
    Created by IFCZT on  2020/1/8 16:20
"""
__author__ = 'IFCZT'
from enum import Enum


class AuthorityEnum(Enum):
    GOD = 10
    SUPER_ADMIN = 9
    ADMIN = 8
    OPERATOR = 7
    USER = 1


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201


