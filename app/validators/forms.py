"""
    Created by IFCZT on  2020/1/8 15:49
"""
from wtforms import StringField, IntegerField, BooleanField

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Forbidden, USER_EXISTS, NICKNAME_EXISTS, ClientTypeError
from app.models.User import User
from app.validators import DataRequired, Regexp, Length as length
from app.validators.base import BaseForm as Form

__author__ = 'IFCZT'


class ClientForm(Form):
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError:
            raise ClientTypeError()
        self.type.data = client


class AccountForm(Form):
    account = StringField(validators=[DataRequired(), length(
        min=4, max=10
    )])
    password = StringField(validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       length(min=2, max=22)])
    auth = StringField(validators=[DataRequired()])
    @staticmethod
    def validate_account(self, value):
        if User.query.filter_by(account=value.data).first():
            raise Forbidden(USER_EXISTS)

    @staticmethod
    def validate_nickname(self, value):
        if User.query.filter_by(nickname=value.data).first():
            raise Forbidden(NICKNAME_EXISTS)


class LoginForm(Form):
    account = StringField(validators=[DataRequired(), length(min=3, max=10)])
    password = StringField(validators=[
        DataRequired(),
        # 密码只能包含字母、数字和 '_'
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])

class PageLimitForm(Form):
    page =  IntegerField(validators=[DataRequired()],default=1)
    limit = IntegerField(validators=[DataRequired()],default=20)

class UserListForm(PageLimitForm):
    u_type = BooleanField(default=True)

class TokenForm(Form):
    token = StringField(validators=[DataRequired()])

class RateForm(Form):
    scur = StringField(validators=[DataRequired()])