"""
    Created by IFCZT on  2020/1/15 14:55
"""
__author__ = 'IFCZT'

from app import create_app
from app.models.base import db
from app.models.User import User

app = create_app()
with app.app_context():
    with db.auto_commit():
        # 创建一个超级管理员
        user = User()
        user.nickname = '陈大海'
        user.password = '123456'
        user.account = 'ifczt'
        user.auth = 2
        db.session.add(user)