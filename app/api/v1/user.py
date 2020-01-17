"""
    Created by IFCZT on  2020/1/8 16:08
"""
from flask import g, jsonify, Response, request

from app.api.v1.token import create_token, auth
from app.libs.enums import AuthorityEnum
from app.libs.error_code import Success, LOGIN_SUCC, LOGOUT_SUCC, USER_INFO_GET, GET_AUTH_SUCC, GET_USER_LIST, \
    SuccessSQL
from app.libs.redprint import Redprint
from app.models.User import User
from app.validators.forms import AccountForm, LoginForm, PageLimitForm, UserListForm

__author__ = 'IFCZT'

api = Redprint('user')


@api.route('', methods=["POST"])
@auth.login_required
def create_account():
    form = AccountForm().validate_for_api()
    User.register_by_account(
        form.nickname.data, form.account.data, form.password.data,
        form.auth.data, g.user.u_id)
    return Success()


@api.route('/login', methods=["POST"])
def login():
    form = LoginForm().validate_for_api()
    data = User.verify(form.account.data, form.password.data)
    data['token'] = create_token(data['u_id'], data['author'])
    return Success(msg=LOGIN_SUCC, data=data)


@api.route('/info', methods=['get'])
@auth.login_required
def get_info():
    user_info = User.query.filter_by(u_id=g.user.u_id).first()
    data = {'token_exp': g.token_exp, 'name': user_info.nickname}
    return Success(msg=USER_INFO_GET, data=data)


# 获取用户组
@api.route('/auth_list', methods=['get'])
@auth.login_required
def get_auth_list():
    data = []
    for item in AuthorityEnum:
        if AuthorityEnum[g.user.author].value > item.value:
            data.append(item.name)
    return Success(GET_AUTH_SUCC, data=data)


@api.route('/list', methods=['post'])
@auth.login_required
def get_list():
    page_box = UserListForm().validate_for_api()
    limit = page_box.limit.data
    page = (page_box.page.data-1)*limit
    u_type = page_box.u_type.data
    if u_type:
        sql = User.query.filter(User.parent==g.user.u_id,User.author!=AuthorityEnum.USER.name)
    else:
        sql = User.query.filter(User.parent==g.user.u_id,User.author==AuthorityEnum.USER.name)
    user_list =sql.limit(limit).offset(page).all()
    total = sql.limit(limit).offset(page).count()
    return SuccessSQL(msg=GET_USER_LIST,data={'list':user_list,'total':total})


@api.route('/logout', methods=["get"])
def logout():
    return Success(LOGOUT_SUCC)
