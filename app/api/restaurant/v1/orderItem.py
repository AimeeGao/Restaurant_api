# 获取用户点菜信息的路由
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.api.restaurant.models.orderItem import OrderItem
from flask import jsonify, g

api = Redprint('order_item')

# 将用户购物车中的信息添加到order_item表中
@api.route('/<int:cid>', methods=['GET'])
@auth.login_required
def add_cart_item_2_order_item(cid):
    uid = g.user.uid
    add_order_item = OrderItem.add_shopping_cart_item_2_order_item(uid, cid)
    return jsonify(add_order_item)

# 获取点餐详情
@api.route('', methods=['GET'])
@auth.login_required
def get_order_item():
    uid = g.user.uid
    get_order_item = OrderItem.get_order_item_info(uid)
    return jsonify(get_order_item)

