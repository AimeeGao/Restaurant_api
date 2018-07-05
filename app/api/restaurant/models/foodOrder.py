from sqlalchemy import Column, String, Integer, Boolean, Numeric, ForeignKey, Float
from flask import url_for
from app.libs.model_base import Base, MixinModelJSONSerializer
from sqlalchemy.orm import relationship
from app.api.restaurant.models.orderItem import OrderItem
from app.api.restaurant.models.menu import Menu
from app.libs.model_base import db
from app.libs.error_code import ParameterException, NotFound
from flask import jsonify, g



# 订单信息
class FoodOrder(Base, MixinModelJSONSerializer):
    __bind_key__ = 'restaurant'

    id = Column(Integer, primary_key=True)

    user  = relationship('User')
    user_id = Column(Integer, ForeignKey('user.id'))


    # 消费总金额
    fee = Column(Float(5,2), nullable=False, default=0)



    # 获取订单信息
    def get_order_info(order_id):
        #num
        #time
        #
        ret_data = {
                "order" :None,
                "order_items": []
                }

        order = FoodOrder.query.filter_by(id = order_id).first_or_404()
        # order_items = OrderItem.query.filter_by(food_order_id=order.id).all()
        order_items = db.session.query(OrderItem.id,OrderItem.user_id,OrderItem.menu_id,OrderItem.num, Menu.name, Menu.price).join(Menu, OrderItem.menu_id==Menu.id).filter(OrderItem.food_order_id==order.id).all()

        ret_data['order'] = order
        for item in order_items:
            ret_data['order_items'].append(dict(zip(item.keys(), item)))
        return ret_data

    # 生成订单FoodOrder信息
    def generate_order(menu_list_info, user_id):
        # 生成一个订单
        food_order = FoodOrder()
        food_order.user_id = user_id
        # 获得用户点菜的id 列表， 并且保存在 orderItem 中
        total_price = 0
        db.session.add(food_order)
        db.session.flush()
        for menu_info in menu_list_info:
            # 防止数据重复添加
            menu_id = menu_info.get('menu_id')
            #根据id找到用户点的菜 并且计算价格
            menu = Menu.query.filter_by(id=menu_id).first()
            if not menu:
                raise ParameterException()
            order_item =  OrderItem()
            order_item.menu_id =menu_id
            order_item.num = menu_info.get('num')
            order_item.food_order_id = food_order.id
            order_item.user_id = user_id
            #累加每道菜的价格
            price = menu.price * order_item.num
            total_price += price
            db.session.add(order_item)

        food_order.fee = total_price
        db.session.commit()
        #return "success"







    #def generate_order(menu_list, user_id):
    #    with db.auto_commit():
    #        food_order = FoodOrder()
    #        food_order.user_id = user_id
    #        total_price = 0
    #        #food_order.fee = each menu.price total sum
    #        for menu in menu_list:
    #            # 查询一个记录 需要找到该数据的id号
    #            menu_id = menu.get['menu_id']
    #            menu = Menu.query.filter_by(id=menu_id).first()
    #            if not menu:
    #                raise NotFound()
    #            orderItem = OrderItem()
    #            orderItem.menu_id = menu_id
    #            orderItem.num = menu.get['num']
    #            orderItem.user_id = user_id
    #            orderItem.food_order_id = food_order.id
    #            price = menu.price
    #            total_price += price
    #            db.session.add(orderItem)
    #        food_order.fee = total_price
    #        db.session.add(food_order)
    #        db.session.commit()
    #        return 'success'

