"""
 Created by 七月 on 2018/5/10.
"""
from app.validators.base import BaseForm as Form
from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError
from app.libs.enums import ClientTypeEnum
from app.api.restaurant.models.user import User

# 基类表单 实现枚举类型验证
class ClientForm(Form):
    account = StringField('用户名', validators=[DataRequired(message='不允许为空'), Length(min=1, max=32, message='用户名长度在1~32个位之间')])
    password = StringField('密码')
    type = IntegerField('类型', validators=[DataRequired(message='不允许为空')])

# 验证基类中的type类型
    def validate_type(self, field):
        try:
            client = ClientTypeEnum(field.data)
        except ValueError as e:
            raise e
        self.type.data = client


# 账号为手机号的用户表单
class UserMobileForm(ClientForm):
    account = IntegerField('手机号', validators=[DataRequired(message='不允许为空'), Regexp(r'^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$', message='不合法的手机号')])
    password = StringField('密码', validators=[DataRequired(message='不允许为空'), Regexp(r'^[A-Za-z0-9*&$#@]{6,22}$', message='密码长度在6~22位之间')])
    nickname = StringField('昵称', validators=[DataRequired(message='不允许为空'), Length(min=2, max=22, message='昵称长度在2~22位')])

    # 验证用户账号是否存在
    def validate_account(self, field):
        if User.query.filter_by(account=field.data).first():
            raise  ValidationError('该手机号已存在')

    # 验证昵称是否存在
    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('该昵称已存在')


"""from wtforms import StringField, IntegerField, PasswordField
from wtforms.validators import DataRequired, length, Email, Regexp, Length, EqualTo, IPAddress
from wtforms import ValidationError
from app.libs.enums import ClientTypeEnum
from app.api.restaurant.models.user import User
from app.validators.base import BaseForm as Form
from app.config.project import devkeys

__author__ = '七月'


class ClientForm(Form):
    account = StringField(validators=[DataRequired(message='不可为空'), length(
        min=5, max=32, message='长度必须在5~32之间'
    )])
    secret = StringField()
    type = IntegerField(validators=[DataRequired(message='不可为空')])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='请输入有效的邮箱')
    ])
    secret = StringField(validators=[
        DataRequired(message='不可为空'),
        # password can only include letters , numbers and "_"
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$', message='密码长度必须在6~22位之间，包含字符、数字和"-"')
    ])
    nickname = StringField(validators=[DataRequired(message='不可为空'),
                                       length(min=2, max=10, message='昵称长度必须在2~10之间')])

    def validate_account(self, value):
        # ValidationError 返回不再清晰
        if User.query.filter_by(email=value.data).first():
            raise ValidationError('该邮箱已经注册过')

    def validate_nickname(self, value):
        if User.query.filter_by(nickname=value.data).first():
            raise ValidationError('该昵称已经存在')


class BookSearchForm(Form):
    q = StringField(validators=[DataRequired(message='不可为空')])


class TokenForm(Form):
    token = StringField(validators=[DataRequired(message='不可为空')])


class DeveloperImoocForm(ClientForm):
    # DataRequired后面记得加()调用一下
    cid = IntegerField(validators=[DataRequired(message='不可为空')])


# 检验重置密码邮箱的格式
class EmailForm(Form):
    email = StringField('电子邮件', validators=[DataRequired(message='不可为空'),
                                            Length(1, 64, message='长度必须在1~64之间'),
                                            Email(message='电子邮箱不符合规范')])


# 重置密码校验
class ResetPasswordForm(Form):
    new_password = PasswordField('新密码', validators=[
        DataRequired(message='不可为空'),
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$', message='密码长度必须在6~22位之间，包含字符、数字和"-"'),
        Length(6, 10, message='密码长度至少需要在6到20个字符之间'),
        EqualTo('confirm_password', message='两次输入的密码不一致')])
    confirm_password = PasswordField('确认新密码', validators=[DataRequired(message='必须确认密码')])


# 更改密码校验
class ChangePasswordForm(ResetPasswordForm):
    old_password = PasswordField('原密码', validators=[DataRequired(message='不可为空')])


# 创建课程检验
class CourseCreateForm(Form):
    name = StringField(validators=[DataRequired(message='不可为空'), length(min=2, max=50, message='长度必须在2~50之间')])
    slogan = StringField(validators=[DataRequired(message='不可为空')])


# 校验receive信息
# ip、devkey、puid、api_sign
class IpInfoForm(Form):
    puid = IntegerField(validators=[DataRequired(message='不可为空')])
    devkey = StringField(validators=[DataRequired(message='不可为空')])
    api_sign = StringField()
    # 113.57.168.162
    ip = StringField(validators=[IPAddress(message='ip地址不符合规范')])

    def validate_devkey(self, value):
        if not devkeys.get(value.data):
            raise ValidationError('不存在该devkey')

# 校验influxdb数据信息
# 暂不需要
# class InfoMeasurementForm(ReceiveInfoForm):
#     uid = IntegerField(validators=[DataRequired()])
#     country = StringField()
#     region = StringField()
#     city = StringField()

"""
