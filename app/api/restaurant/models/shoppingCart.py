from sqlalchemy import Column, String, Integer, Boolean,ForeignKey
from flask import url_for
from app.libs.model_base import Base,db, MixinModelJSONSerializer
from sqlalchemy.orm import relationship
from app.api.restaurant.models.foodOrder import FoodOrder
from app.api.restaurant.models.menu import Menu
#from app.api.restaurant.models.orderItem import OrderItem

# 购物车表
class ShoppingCart(Base, MixinModelJSONSerializer):
    __bind_key__ = 'restaurant'
    id = Column(Integer, primary_key=True)

    # 关联用户表
    user = relationship('User')
    user_id = Column(Integer, ForeignKey('user.id'))
    num = Column(Integer, default=1)
    # 点的菜, 每个菜的单价
    menu = relationship('Menu')
    menu_id = Column(Integer, ForeignKey('menu.id'))
    # # 点菜的数量和消费的总金额
    # order_item = relationship('OrderItem')
    # order_item_id = Column(Integer, ForeignKey('order_item.id'))

# 添加购物车 == 用户点菜
    @staticmethod
    def add_menu(user_id, menu_id):
        #| id          | int(11)     | NO   | PRI | NULL    | auto_increment |
        #| menu_id     | int(11)     | YES  | MUL | NULL    |                |
        #| user_id     | int(11)     | YES  | MUL | NULL    |                |
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
            return True

    def get_menus(user_id):
	# print(db.session.query(Bind.bindid, Account.gameuid, Account.nickname). \
    	# join(Account, Account.gameuid==Bind.fromid). \
    	# filter(Bind.toid == 1000))
        results = db.session.query(ShoppingCart.id,Menu.name,ShoppingCart.num).join(Menu,ShoppingCart.menu_id==Menu.id).filter(ShoppingCart.user_id==user_id).all()
        return [dict(zip(result.keys(), result)) for result in results]





