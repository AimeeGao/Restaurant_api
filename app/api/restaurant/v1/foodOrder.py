# 订单信息路由
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from flask import g, jsonify
from app.api.restaurant.models.foodOrder import FoodOrder

api = Redprint('food_order')

# 用户获取食物订单
@api.route('/<int:uid>', methods=['GET'])
#@auth.login_required
def get_food_order(uid):
    order_info = FoodOrder.get_menu(uid)
    return jsonify(order_info)
    #return 'get_food'

