"""
    Created by IFCZT on  2020/1/8 16:08
"""
from flask import jsonify

from app.libs.redpring import Redprint
from app.models.User import User
from app.models.base import db
from app.validators.forms import AccountForm

__author__ = 'IFCZT'

api = Redprint('user')

@api.route('',methods=["POST"])
def create_account():
    form =  AccountForm().validate_for_api()
    User.register_by_account(form.nickname.data,form.account.data,form.password.data)
    return jsonify({'uid':1})