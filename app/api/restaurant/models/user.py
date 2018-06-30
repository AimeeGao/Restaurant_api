"""
 Created by 七月 on 2018/5/11.
"""
from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, g
from app.libs.error_code import PasswordCheckException, UserNotExistException, MuidDuplicateException
from app.libs.model_base import Base, db, MixinModelJSONSerializer
from app.libs.error_code import UserNotExistException, PasswordCheckException

__author__ = '七月'

# 用户信息
class User(Base, MixinModelJSONSerializer):
    __bind_key__ = 'restaurant'
    id = Column(Integer, primary_key=True)
    account = Column(String(32), unique=True, nullable=False)
    nickname = Column(String(24), unique=True, nullable=False)
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(100))

    def _set_fields(self):
        """设置序列化时隐藏的字段"""
        self._exclude = ['password']


    @property
    def password(self):
        return self._password

    # 密码加密
    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    # 用户手机注册 添加一条记录到数据库
    @staticmethod
    def register_by_mobile(account, password, nickname):
        with db.auto_commit():
            user = User()
            user.account = account
            user.password = password
            user.nickname = nickname
            db.session.add(user)


    # 验证加盐密码 返回True/False
    def check_password(self, password):
        if not self._password:
            return False
        return check_password_hash(self._password, password)

    # 验证表单账号及对应的密码
    @staticmethod
    def verify(account, password):
        user = User.query.filter_by(account=account).first()
        if not user:
            raise UserNotExistException()

        if not user.check_password(password):
            raise PasswordCheckException()

        # account password
        scope = 'AdminScope' if user.auth == 2 else 'UserScope'
        return {
                'uid':user.id,
                'scope':scope
                }







        """class User(Base, MixinModelJSONSerializer):
    __bind_key__ = 'persona'
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True, nullable=False)
    mobile = Column(String(16), unique=True)
    auth = Column(SmallInteger, default=1)
    # （慕课网id）muid必须不同
    muid = Column(String(24), unique=True)
    _password = Column('password', String(100))

    def _set_fields(self):
            设置序列化时隐藏的字段
        self._exclude = ['password']

    # 获取密码字段&对密码字段加密
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, orgin):
        self._password =  generate_password_hash(orgin)

    #静态实现注册功能
    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)

    def check_password(self, password):
        if not self._password:
            return False
        return check_password_hash(self._password, password)

    # 验证用户名 密码后，返回user.id scope
    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(email=email).first()
        if not user:
            raise UserNotExistException()

        if not user.check_password(password):
            raise PasswordCheckException()

        # 验证成功的用户携带一个scope
        scope =  'AdminScope' if user.auth == 2 else 'UserScope'

        return {'uid':user.id, 'scope':scope}

    # 重设密码
    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        uid = data.get('id')
        with db.auto_commit():
            user = User.query.get(uid)
            user.password = new_password
        return True

    # 修改密码
    @staticmethod
    def change_password(old_password, new_password):
        uid = g.user.uid
        with db.auto_commit():
            user = User.query.get(uid)
            if not user:
                return False
            if user.check_password(old_password):
                user.password = new_password
                return True
        # ** Q **
        return False

"""











"""
    def generate_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({
            'id': self.id
        }).decode('utf-8')

    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        uid = data.get('id')
        with db.auto_commit():
            user = User.query.get(uid)
            user.password = new_password
        return True

    @staticmethod
    def change_password(old_password, new_password):
        uid = g.user.uid
        with db.auto_commit():
            user = User.query.get(uid)
            if not user:
                return False
            # 旧密码校验成功
            if user.check_password(old_password):
                user.password = new_password
                return True
        return False

    @staticmethod
    def check_muid(muid, uid):
        # muid不能被两个用户同时绑定
        fi = User.query.filter_by(muid=muid).first()
        if not fi:
            user = User.query.filter_by(id=uid).first()
            if not user.muid:
                with db.auto_commit():
                    user.muid = muid
                    db.session.add(user)
        else:
            if fi.id != uid:
                raise MuidDuplicateException()
"""
