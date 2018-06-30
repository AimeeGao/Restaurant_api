"""
 Created by 七月 on 2018/5/28.
"""
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Numeric
from flask import url_for
from app.libs.model_base import Base, MixinModelJSONSerializer
from sqlalchemy.orm import relationship


# 订单详情表

#cid = Column(Integer, ForeignKey('course.id'))
class OrderItem(Base, MixinModelJSONSerializer):
    __bind_key__ = 'restaurant'
    id = Column(Integer, primary_key=True)

    menu = relationship('Menu')
    menu_id = Column(Integer, ForeignKey('menu.id'))

    food_order = relationship('FoodOrder')
    food_order_id = Column(Integer, ForeignKey('food_order.id'))

    price = Column(Numeric(5,2),nullable=False)


