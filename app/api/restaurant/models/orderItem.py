"""
 Created by 七月 on 2018/5/28.
"""
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Numeric, Float
from flask import url_for, jsonify
from app.libs.model_base import Base, MixinModelJSONSerializer, db
from sqlalchemy.orm import relationship
from app.api.restaurant.models.menu import Menu
from app.api.restaurant.models.foodOrder import FoodOrder
from app.api.restaurant.models.shoppingCart import ShoppingCart

# 订单详情表 点了什么菜

#cid = Column(Integer, ForeignKey('course.id'))
class OrderItem(Base, MixinModelJSONSerializer):
    __bind_key__ = 'restaurant'
    id = Column(Integer, primary_key=True)

    user = relationship('User')
    user_id = Column(Integer, ForeignKey('user.id'))

    #menu = relationship('Menu')
    #menu_id = Column(Integer, ForeignKey('menu.id'))

    shopping_cart = relationship('ShoppingCart')
    shopping_cart_id = Column(Integer, ForeignKey('shopping_cart.id'))

    #food_order = relationship('FoodOrder')
    #food_order_id = Column(Integer, ForeignKey('food_order.id'))

    name = Column(String(32))
    num = Column(Integer, default=1)
    price = Column(Float(10,2))

    # 将用户购物车中的信息添加到order_item表中
    # 业务逻辑有问题
    @staticmethod
    def add_shopping_cart_item_2_order_item(user_id, cart_id):
        # 查询order_item表中是否已经存在该订单
        order_item = OrderItem.query.filter_by(id=cart_id).first()
        if order_item:
            order_item.num += 1
        with db.auto_commit():
            order_item = OrderItem()
            order_item.user_id = user_id
            order_item.shopping_cart_id = cart_id
            db.session.add(order_item)
        return True

    # 获取用户点菜信息
    @staticmethod
    #print(db.session.query(Bind.bindid, Account.gameuid, Account.nickname). \
    #join(Account, Account.gameuid==Bind.fromid). \
    #filter(Bind.toid == 1000))
    def get_order_item_info(user_id):
        #import pdb
        #pdb.set_trace()
        results = db.session.query(OrderItem.id,OrderItem.user_id, Menu.name, Menu.price, ShoppingCart.num).join(ShoppingCart, OrderItem.shopping_cart_id==ShoppingCart.id).join(Menu, ShoppingCart.menu_id==Menu.id).filter(OrderItem.user_id==user_id).all()
        return [dict(zip(result.keys(), result)) for result in results]


