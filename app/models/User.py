"""
    Created by IFCZT on  2020/1/8 15:49
"""
from uuid import uuid4

from pip._vendor.appdirs import unicode
from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.error_code import AuthFailed, USER_NOT_EXISTS
from app.models.base import Base, db

__author__ = 'IFCZT'


class User(Base):
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    u_id = Column(String(128), unique=True)
    account = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    author = Column(String(24), default=1)
    parent =  Column(String(128), unique=True)
    state = Column(SmallInteger,default=1)
    _password = Column('password', String(100))

    def keys(self):
        return ['id', 'account', 'nickname', 'author','state']

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    # 声明静态注册账号方法
    @staticmethod
    def register_by_account(nickname, account, password, author, u_id):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.account = account
            user.password = password
            user.author = author
            user.u_id = unicode(uuid4())
            user.parent = u_id
            db.session.add(user)

    @staticmethod
    def verify(account, password):
        user = User.query.filter_by(account=account).first_or_404(USER_NOT_EXISTS)
        if not user.check_password(password):
            raise AuthFailed()
        return {'u_id': user.u_id, 'author': user.author}

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)
