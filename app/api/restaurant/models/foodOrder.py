from sqlalchemy import Column, String, Integer, Boolean, Numeric, ForeignKey, Float
from flask import url_for
from app.libs.model_base import Base, MixinModelJSONSerializer
from sqlalchemy.orm import relationship

# 订单信息
class FoodOrder(Base, MixinModelJSONSerializer):
    __bind_key__ = 'restaurant'

    id = Column(Integer, primary_key=True)

    # 用户所点的菜
    order_item = relationship('OrderItem')
    order_item_id = Column(Integer, ForeignKey('order_item.id'))

    user  = relationship('User')
    user_id = Column(Integer, ForeignKey('user.id'))
    # 消费金额
    fee = Column(Float(5,2), nullable=False, default=0)

    # 订单数量
    order_num = Column(Integer, nullable=False)

    # 获取用户订单信息
    @staticmethod
    def get_order(uid):
        order_list = FoodOrder.query.filter_by(user_id=uid).first_or_404()
        return order_list





