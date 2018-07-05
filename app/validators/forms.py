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


