# 获取用户点菜信息的路由
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.api.restaurant.models.orderItem import OrderItem
from flask import jsonify, g

api = Redprint('order_item')

# orderitem 前端传来的数据格式
# [{
#     "user_id":1,
#     "menu_id":1
#   },
#   {
#     "user_id":2,
#     "menu_id":2
#   }


#  ]


# *** orderItem表中的信息应与FoodOrder表一起生成 同一个transaction ***
#@api.route('/<int:mid>', methods=['GET'])
#@auth.login_required
# def generate_order_item(mid):
#     uid = g.user.uid
#     add_order_item = OrderItem.generate_order_item_info(uid, mid)
#     return jsonify(add_order_item)

# 获取该用户的点餐详情
# @api.route('', methods=['GET'])
# @auth.login_required
# def get_order_item():
#     uid = g.user.uid
#     get_order_item = OrderItem.get_order_item_info(uid)
#     return jsonify(get_order_item)

