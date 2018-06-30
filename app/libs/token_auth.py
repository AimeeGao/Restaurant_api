"""
 Created by 七月 on 2018/5/13.
"""

from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from flask import current_app, g, request
from app.libs.error_code import AuthFailed, Forbidden
from collections import namedtuple
from app.libs.scope import is_in_scope

auth = HTTPBasicAuth()
User = namedtuple('User',['uid', 'type', 'scope'])

# @auth.get_password 只能获取明文密码

# True/False
@auth.verify_password
def verify_password(token, password):
    # http token
    # header key:value
    # key: Authorization
    # value: base64(account:pwd)
    user_info = verify_auth_token(token)
    if not user_info:
        return Flase
    # 将用户的相关信息保存到g中，在视图中使用
    g.user = user_info
    return True


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    # 解密token
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token is invalid', error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired', error_code=1003)

    # 获取token中的有关信息
    uid = data['uid']
    ac_type = data['type']
    scope = data['scope']

    # 添加权限验证
    allow = is_in_scope(scope, request.endpoint)
    if not allow:
        raise Forbidden(msg='没有权限访问该页面')
    return User(uid, ac_type, scope)




















""" from collections import namedtuple

from flask import current_app, g, request
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer \
    as Serializer, BadSignature, SignatureExpired

from app.libs.error_code import AuthFailed, Forbidden
from app.libs.scope import is_in_scope

__author__ = '七月'

auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'ac_type', 'scope'])


@auth.verify_password
def verify_password(token, password):
    # token
    # HTTP 账号密码
    # header key:value
    # account  qiyue
    # 123456
    # key=Authorization
    # value =basic base64(qiyue:123456)
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        # request
        g.user = user_info
        return True


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token is invalid',
                         error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired',
                         error_code=1003)
    uid = data['uid']
    ac_type = data['type']
    scope = data['scope']
    # request 视图函数
    allow = is_in_scope(scope, request.endpoint)
    if not allow:
        raise Forbidden()
    return User(uid, ac_type, scope)
"""

