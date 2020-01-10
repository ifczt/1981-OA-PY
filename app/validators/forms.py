"""
    Created by IFCZT on  2020/1/8 15:49
"""
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp
from wtforms import ValidationError

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Forbidden
from app.models.User import User
from app.validators.base import BaseForm as Form

__author__ = 'IFCZT'


class ClientForm(Form):
    account = StringField(validators=[DataRequired(message='不允许为空'), length(
        min=5, max=32
    )])
    password = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class AccountForm(ClientForm):
    account = StringField(validators=[
        Email(message='邮箱不合法')
    ])
    password = StringField(validators=[
        DataRequired(),
        # password can only include letters , numbers and "_"
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       length(min=2, max=22)])


    def validate_account(self,value):
        if User.query.filter_by(email=value.data).first():
            raise Forbidden()




class TokenForm(Form):
    token = StringField(validators=[DataRequired()])
