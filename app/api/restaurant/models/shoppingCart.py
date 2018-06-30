from sqlalchemy import Column, String, Integer, Boolean,ForeignKey
from flask import url_for
from app.libs.model_base import Base, MixinModelJSONSerializer
from sqlalchemy.orm import relationship


# 购物车表
class ShoppingCart(Base, MixinModelJSONSerializer):
    __bind_key__ = 'restaurant'
    id = Column(Integer, primary_key=True)

    # 点的菜, 每个菜的单价
    menu = relationship('Menu')
    menu_id = Column(Integer, ForeignKey('menu.id'))

    # 点菜的数量和消费的总金额
    food_order = relationship('FoodOrder')
    food_order_id = Column(Integer, ForeignKey('food_order.id'))


