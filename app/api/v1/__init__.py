"""
    Created by IFCZT on  2020/1/8 16:06
"""
from flask import Blueprint

from app.api.v1 import user, token

__author__ = 'IFCZT'

# 注册蓝图
def create_blueprint():
    bp = Blueprint('v1',__name__)
    user.api.register(bp)
    token.api.register(bp)
    return bp
