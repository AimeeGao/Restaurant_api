from app.libs.redprint import Redprint
from app.validators.forms import ClientForm
from app.libs.enums import ClientTypeEnum
from flask import jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app.api.restaurant.models.user import User
from flask import current_app

# 生成token路由 返回token json数据
api = Redprint('token')

@api.route('', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()

    #import pdb
    #pdb.set_trace()
    promise = {
            ClientTypeEnum.USER_MOBILE : User.verify
            }

    # uid, scope
    identity = promise[ClientTypeEnum(form.type.data)](form.account.data, form.password.data)

    expiration = current_app.config['TOKEN_EXPIRATION']
    # token的类型为bytes
    token = generate_auth_token(identity['uid'], form.type.data, identity['scope'], expiration)
    t = {
            'token':token.decode('ascii')

        }
    return jsonify(t), 201

# 生成token
def generate_auth_token(uid, ac_type, scope, expiration=7200):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in = expiration)
    return s.dumps({
        'uid':uid,
        'type':ac_type.value,
        'scope':scope
        })














"""
 Created by 七月 on 2018/5/13.
"""
# from flask import current_app, jsonify

# from app.libs.enums import ClientTypeEnum
# from app.libs.error_code import AuthFailed
# from app.libs.redprint import Redprint
# from app.api.restaurant.models.user import User
# from app.validators.forms import ClientForm, TokenForm
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, \
#     BadSignature

# api = Redprint('token')

# __author__ = '七月'


# @api.route('', methods=['POST'])
# def get_token():
#     """ 获得令牌
#         发送json数据进行获取
#         ---
#         parameters:
#           - name: account
#             in: body
#             type: string
#             required: true
#             example: 123456@qq.com
#           - name: secret
#             in: body
#             type: string
#             required: true
#             example: 123456
#           - name: type
#             in: body
#             type: int
#             required: true
#             example: 100
#         responses:
#           200:
#             description: 返回信息
#             examples:
#               success : {"token": "eyJhbGciOiJIUzI1NiIsImlhdCI6MTUyODM0Njg0NCwiZXhwIjoxNTMwOTM4ODQ0fQ.eyJ1aWQiOjIsInR5cGUiOjEwMCwic2NvcGUiOiJVc2VyU2NvcGUifQ.fzMmFcUrWNCAIOf33VM_j5Yz5CQdnDjcwlimQmqc0eU"}
#     """
#     form = ClientForm().validate_for_api()
#     promise = {
#         ClientTypeEnum.USER_EMAIL: User.verify,
#     }
#     identity = promise[ClientTypeEnum(form.type.data)](
#         form.account.data,
#         form.secret.data
#     )
#     # Token
#     expiration = current_app.config['TOKEN_EXPIRATION']
#     token = generate_auth_token(identity['uid'],
#                                 form.type.data,
#                                 identity['scope'],
#                                 expiration)
#     t = {
#         'token': token.decode('ascii')
#     }
#     return jsonify(t), 201


# @api.route('/secret', methods=['POST'])
# def get_token_info():
#     """
#     获取令牌信息
#     发送token字段获取消息
#     ---
#     parameters:
#       - name: token
#         in: body
#         type: string
#         required: true
#         example: ijihjhjkhjkhkhkjhkjh
#     """
#     form = TokenForm().validate_for_api()
#     s = Serializer(current_app.config['SECRET_KEY'])
#     try:
#         data = s.loads(form.token.data, return_header=True)
#     except SignatureExpired:
#         raise AuthFailed(msg='token is expired', error_code=1003)
#     except BadSignature:
#         raise AuthFailed(msg='token is invalid', error_code=1002)

#     r = {
#         'scope': data[0]['scope'],
#         'create_at': data[1]['iat'],
#         'expire_in': data[1]['exp'],
#         'uid': data[0]['uid']
#     }
#     return jsonify(r)


# # 一周 7 * 24 * 3600
# def generate_auth_token(uid, ac_type, scope=None,
#                         expiration=7200):
#     """生成令牌"""
#     s = Serializer(current_app.config['SECRET_KEY'],
#                    expires_in=expiration)
#     return s.dumps({
#         'uid': uid,
#         'type': ac_type.value,
#         'scope': scope
#     })
