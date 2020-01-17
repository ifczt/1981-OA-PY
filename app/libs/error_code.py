"""
    Created by IFCZT on  2020/1/8 16:32
"""
from flask import request, json,jsonify

from app.libs.error import APIException

__author__ = 'IFCZT'

class SuccessSQL():
    code = 200
    msg = '操作成功'
    data = []
    def __new__(cls, *args, **kwargs):
        obj = {'code': cls.code, 'msg': kwargs['msg'] if 'msg' in kwargs else cls.msg, 'data': kwargs['data']}
        return  jsonify(obj)


class Success(APIException):
    code = 201
    msg = '操作成功'
    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            code=self.code,
            data=self.data,
            request=request.method + ' ' + self.get_url_no_param()
        )
        text = json.dumps(body)
        return text


class DeleteSuccess(Success):
    code = 202
    msg = '删除成功'


class ServerError(APIException):
    code = 500
    msg = '抱歉，我们引起了一个错误！o(╯□╰)o'


class ClientTypeError(APIException):
    code = 400
    msg = '无效客户端'


class ParameterException(APIException):
    code = 400
    msg = '参数无效'


class NotFound(APIException):
    code = 404
    msg = '找不到该资源 O__O...'


class AuthFailed(APIException):
    code = 401
    msg = '身份验证失败'


class Forbidden(APIException):
    code = 403
    msg = '权限不足，无法完成此操作'

# ERROR
USER_EXISTS = '用户已存在'
USER_NOT_EXISTS = '找不到该用户'
NICKNAME_EXISTS = '昵称已存在'
PARAM_REQUIRE = '参数不允许为空'
PARAM_FAILED = '参数未通过校验'
PARAM_LENGTH = '参数长度应该在%(min)d和%(max)d之间.'
URL_NOT_EXISTS = '访问路径不存在'
TOKEN_INVALID = '令牌无效'
TOKEN_EXPIRED = '令牌已过期'
RATE_NOT_FOUND = '获取汇率出现错误'
# SUCCESS
LOGIN_SUCC = '登录成功'
LOGOUT_SUCC = '退出账号成功'
USER_INFO_GET = '获取用户信息成功'
REGAIN_TOKEN = '令牌续签成功'
GET_AUTH_SUCC = '获取用户组列表成功'
GET_USER_LIST = '获取用户列表成功'
GET_RATE = '获取汇率成功'
