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






