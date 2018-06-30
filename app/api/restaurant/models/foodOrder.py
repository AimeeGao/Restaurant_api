from sqlalchemy import Column, String, Integer, Boolean, Numeric, ForeignKey, Float
from flask import url_for
from app.libs.model_base import Base, MixinModelJSONSerializer
from sqlalchemy.orm import relationship

# 订单信息
class FoodOrder(Base, MixinModelJSONSerializer):
    __bind_key__ = 'restaurant'

    id = Column(Integer, primary_key=True)

    # 点的菜名，和所点菜的单价
    menu = relationship('Menu')
    menu_id = Column(Integer, ForeignKey('menu.id'))

    user  = relationship('User')
    user_id = Column(Integer, ForeignKey('user.id'))
    # 消费金额
    fee = Column(Float(5,2), nullable=False, default=0)

    # 点菜数量
    order_num = Column(Integer, nullable=False)

    # 获取用户订单信息
    @staticmethod
    def get_menu(uid):
        order_list = FoodOrder.query.filter_by(user_id=uid).first_or_404()
        return order_list





