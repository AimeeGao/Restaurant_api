# 用户信息页面
from app.libs.redprint import Redprint
from app.api.restaurant.models.user import User
from app.libs.token_auth import auth
from flask import jsonify, g

api = Redprint('user')

# superadmin 获取用户信息
@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    # 获取到所有用户的信息
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)

# 获取用户个人信息
@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    # g 变量获取User信息
    uid = g.user.uid
    # select * from User where id = uid
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)

@api.route('/get/<int:uid>', methods=['GET'])
#@auth.login_required
def get_user_id(uid):
    user_id = User.get_uid(uid)
    return jsonify(user_id)
