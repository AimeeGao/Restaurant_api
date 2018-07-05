"""
 Created by 七月 on 2018/5/12.
"""
from werkzeug.exceptions import HTTPException

from app.libs.error import APIException

__author__ = '七月'


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class Failed(APIException):
    code = 404
    msg = 'failed'
    error_code = 10008


class DeleteSuccess(Success):
    code = 202
    error_code = 1


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999


class ClientTypeError(APIException):
    # 400 401 403 404
    # 500
    # 200 201 204
    # 301 302
    code = 400
    msg = 'client is invalid'
    error_code = 10006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 10000


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found O__O...'
    error_code = 10001


class AuthFailed(APIException):
    code = 401
    error_code = 10005
    msg = 'authorization failed'


class Forbidden(APIException):
    code = 403
    error_code = 10004
    msg = 'forbidden, not in scope'


class PasswordCheckException(APIException):
    code = 401
    msg = 'password check failed'
    error_code = 20003



