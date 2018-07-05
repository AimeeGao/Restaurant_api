# 订单信息路由
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from flask import g, jsonify, request
from app.api.restaurant.models.foodOrder import FoodOrder
from app.api.restaurant.models.menu import Menu
import json

api = Redprint('food_order')

# 前端发过来的信息源自shopping_cart表中的menu_id num
# FoodOrder表包含一个订单信息表，和多个orderItem表中的信息
#  {"order_info" :[{
# 	"menu_id":"1",
# 	"num":2
# },{
# 	"menu_id":"3",
# 	"num":2
# },
# {
# 	"menu_id":"2",
# 	"num":3
# }
# ]}

# 生成FoodOrder信息
@api.route('/', methods=['POST'])
@auth.login_required
def generate_food_order():
    # menus_id_list[]
    user_id = g.user.uid
    # 调用生成food_order方法
    order_info = FoodOrder.generate_order(request.get_json()['order_info'], user_id)
    return jsonify(order_info)

# 获取订单
@api.route('/<int:user_id>', methods=['GET'])
def get_food_order(user_id):
    order_info = FoodOrder.get_order_info(user_id)
    return jsonify(order_info)

