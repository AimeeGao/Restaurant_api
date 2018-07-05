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






