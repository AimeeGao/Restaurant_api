from sqlalchemy import Column, String, Integer, Boolean,ForeignKey
from flask import url_for
from app.libs.model_base import Base,db, MixinModelJSONSerializer
from sqlalchemy.orm import relationship
from app.api.restaurant.models.foodOrder import FoodOrder
from app.api.restaurant.models.menu import Menu

# 购物车表
class ShoppingCart(Base, MixinModelJSONSerializer):
    __bind_key__ = 'restaurant'
    id = Column(Integer, primary_key=True)

    user = relationship('User')
    user_id = Column(Integer, ForeignKey('user.id'))
    num = Column(Integer, default=1)
    menu = relationship('Menu')
    menu_id = Column(Integer, ForeignKey('menu.id'))

    # # 点菜的数量和消费的总金额
    # order_item = relationship('OrderItem')
    # order_item_id = Column(Integer, ForeignKey('order_item.id'))

# 添加购物车 == 用户点菜
    @staticmethod
    def generate_menu(user_id, menu_id):
        with db.auto_commit():
            menu = ShoppingCart.query.filter_by(menu_id=menu_id).first()
            if menu:
                menu.num += 1
            cart = ShoppingCart()
            cart.menu_id = menu_id
            cart.user_id = user_id
            db.session.add(cart)
            # order_item_info = ShoppingCart.query.filter_by(order_item_id=mid).first_or_404()
            # order_item_info.name = menu_info_list.name
            # order_item_info.price = menu_info_list.price
            # order_item_info.num = menu_info_list.num
            # db.session.add(order_item_info)
            return 'Success'

    def get_menus(user_id):
        results = db.session.query(ShoppingCart.num,Menu.name,Menu.price).join(Menu,ShoppingCart.menu_id==Menu.id).filter(ShoppingCart.user_id==user_id).all()
        return [dict(zip(result.keys(), result)) for result in results]





