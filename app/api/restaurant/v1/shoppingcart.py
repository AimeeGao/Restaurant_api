# 获取购物车信息路由

from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.api.restaurant.models.shoppingCart import ShoppingCart
from flask import g,jsonify

api = Redprint('shopping_cart')

# 向购物车中添加菜
@api.route('/<int:mid>', methods=['GET'])
@auth.login_required
def add_shopping_cart(mid):
    uid = g.user.uid
    add_menu = ShoppingCart.generate_menu(uid, mid)
    return jsonify(add_menu)

# 获取用户本人购物车中的内容
@api.route('/', methods=['GET'])
@auth.login_required
def get_shopping_cart():
    uid = g.user.uid
    # menus = ShoppingCart.query.filter_by(user_id=uid).all()
    shopping_cart_info = ShoppingCart.get_menus(uid)
    return jsonify(shopping_cart_info)


