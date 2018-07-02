""" Created by 七月 on 2018/5/8.
"""
from flask import Blueprint
from app.api.restaurant.v1 import client, token, user, menu, foodOrder, orderItem, shoppingcart
__author__ = '七月'


def create_blueprint_v1():
    bp_v1 = Blueprint('restaurant_v1', __name__)

    client.api.register(bp_v1)
    token.api.register(bp_v1)
    user.api.register(bp_v1)
    menu.api.register(bp_v1)
    foodOrder.api.register(bp_v1)
    orderItem.api.register(bp_v1)
    shoppingcart.api.register(bp_v1)
    # user.api.register(bp_v1)
    # client.api.register(bp_v1)
    # token.api.register(bp_v1)
    # course.api.register(bp_v1)
    # dev.api.register(bp_v1)
    return bp_v1
