"""
    Created by IFCZT on  2020/1/8 16:08
"""
from collections import namedtuple

from flask import current_app, g
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, \
    BadSignature

from app.libs.error_code import AuthFailed, TOKEN_EXPIRED, TOKEN_INVALID, Success, REGAIN_TOKEN
from app.libs.redprint import Redprint

api = Redprint('token')

__author__ = 'IFCZT'


def create_token(u_id, author):
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(u_id, author, expiration)
    return token.decode('ascii')


# 生成令牌
def generate_auth_token(u_id, author, expiration=7200):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({'u_id': u_id, 'author': author})


auth = HTTPTokenAuth()
UserTuple = namedtuple('User', ['u_id', 'author'])


@auth.verify_token
def verify_token(token):
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        g.user = user_info
        return True


# 验证token
def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token, return_header=True)
    except BadSignature:
        raise AuthFailed(TOKEN_INVALID)
    except SignatureExpired:
        raise AuthFailed(TOKEN_EXPIRED)
    g.token_exp = data[1]['exp']
    u_id = data[0]['u_id']
    author = data[0]['author']
    return UserTuple(u_id, author)


@api.route('', methods=['get'])
@auth.login_required
def regain():
    data = create_token(g.user.u_id)
    return Success(msg=REGAIN_TOKEN, data=data)
