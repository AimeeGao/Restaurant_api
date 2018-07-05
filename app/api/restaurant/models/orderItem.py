from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Numeric, Float
from flask import url_for, jsonify
from app.libs.model_base import Base, MixinModelJSONSerializer, db
from sqlalchemy.orm import relationship
from app.api.restaurant.models.menu import Menu

# 订单详情表 点了什么菜

#cid = Column(Integer, ForeignKey('course.id'))
class OrderItem(Base, MixinModelJSONSerializer):
    __bind_key__ = 'restaurant'
    id = Column(Integer, primary_key=True)

    user = relationship('User')
    user_id = Column(Integer, ForeignKey('user.id'))

    menu = relationship('Menu')
    menu_id = Column(Integer, ForeignKey('menu.id'))

    # 一个购物车对应多个OrderItem
    #shopping_cart = relationship('ShoppingCart')
    #shopping_cart_id = Column(Integer, ForeignKey='shopping_cart.id')

    # 一个订单对应多个OrderItem
    food_order = relationship('FoodOrder')
    food_order_id = Column(Integer, ForeignKey('food_order.id'))

    num = Column(Integer, default=1)

    # 生成点餐表
    # 业务逻辑有问题
    #@staticmethod
    #def generate_order_item_info(user_id, menu_id, num):
        # 查询order_item表中是否已经存在该订单
        #begin_trasaction
        # insert a order valuese(1,2,3,4,5);
        # insert a order valuese(1,2,3,4,5);
        # insert a order valuese(1,2,3,4,5);
        #
        # insert a order valuese(1,2,3,4,5);
        # insert a order valuese(1,2,3,4,5);
        # insert a order valuese(1,2,3,4,5);
        # insert a order valuese(1,2,3,4,5);
        #
        # if (fail) {
        # rollback()
        # else {
        #  commit()
        #}
        #}
        # update
        #commit(transaction);
        #order_item = OrderItem.query.filter_by(id=menu_id).first()

        #if order_item:
        #    order_item.num += 1
        #with db.auto_commit():
            # order_item = OrderItem()
            # order_item.user_id = user_id
            # order_item.menu_id = menu_id
            # db.session.add(order_item)
        # return True

    # 获取用户点菜信息
    #@staticmethod
    #print(db.session.query(Bind.bindid, Account.gameuid, Account.nickname). \
    #join(Account, Account.gameuid==Bind.fromid). \
    #filter(Bind.toid == 1000))
    #def get_order_item_info(user_id):
#        results = db.session.query(OrderItem.id,OrderItem.user_id, Menu.name, Menu.price, ShoppingCart.num).join(ShoppingCart, OrderItem.shopping_cart_id==ShoppingCart.id).join(Menu, ShoppingCart.menu_id==Menu.id).filter(OrderItem.user_id==user_id).all()
#        return [dict(zip(result.keys(), result)) for result in results]
        # results = db.session.query(OrderItem.id,OrderItem.user_id, Menu.name, Menu.price).join(Menu, OrderItem.menu_id==Menu.id).filter(OrderItem.user_id==user_id).all()
        # return [dict(zip(result.keys(), result)) for result in results]



