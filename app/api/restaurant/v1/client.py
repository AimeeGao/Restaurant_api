"""
 Created by 七月 on 2018/5/10.
"""
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm, UserMobileForm
from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.api.restaurant.models.user import User

# 用户注册路由

api = Redprint('client')
@api.route('/register', methods=['POST'])
def client_register():
    # self.errors type验证
    form = ClientForm().validate_for_api()

    # 方便多种类型用户注册
    promise = {
            ClientTypeEnum.USER_MOBILE : _register_user_by_mobile
            }
    promise[form.type.data]()
    return Success(msg='注册成功')


def _register_user_by_mobile():
    form = UserMobileForm().validate_for_api()
    User.register_by_mobile(form.account.data, form.password.data, form.nickname.data)





# from app.api.restaurant.v1.token import generate_auth_token
# from flask import jsonify, current_app
# from app.libs.redprint import Redprint
# from app.api.restaurant.models.user import User
# from app.validators.forms import ClientForm, UserEmailForm
# from app.libs.enums import ClientTypeEnum

# __author__ = '七月'

# api = Redprint('client')


# @api.route('/register', methods=['POST'])
# def create_client():
#     """ 用户注册
#         发送json数据进行注册(注册为开发者的type为300)
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
#           - name: nickname
#             in: body
#             type: string
#             required: true
#             example: pedro
#         responses:
#           200:
#             description: 返回信息
#             examples:
#               success : {"error_code": 0,"msg": "ok","request": "POST /restaurant/v1/client/register"}
#     """
#     form = ClientForm().validate_for_api()
#     promise = {
#         ClientTypeEnum.USER_EMAIL: __register_user_by_email,
#     }
#     promise[form.type.data]()

#     # Token
#     identity = User.verify(form.account.data, form.secret.data)
#     expiration = current_app.config['TOKEN_EXPIRATION']
#     token = generate_auth_token(identity['uid'],
#                                 form.type.data,
#                                 identity['scope'],
#                                 expiration)
#     t = {
#         'token': token.decode('ascii')
#     }
#     return jsonify(t), 201


# def __register_user_by_email():
#     form = UserEmailForm().validate_for_api()
#     User.register_by_email(form.nickname.data,
#                            form.account.data,
#                            form.secret.data)
