from app.libs.redprint import Redprint
from flask import g, jsonify
from app.libs.token_auth import auth
from app.api.restaurant.models.menu import Menu
from app.api.restaurant.view_model.menu import MenuCollection

api = Redprint('menu')

# 获取菜单信息
@api.route('', methods=['GET'])
@auth.login_required
def get_menu():
    # query.all() 列表 [<Menu 1>] 列表中包含一个Menu对象
    menu_list = Menu.query.filter_by(status=1).all()
    # return jsonify(menu_list) 返回Menu表中所有字段的信息
    # 返回指定字段信息
    menu_collection = MenuCollection(menu_list)
    return jsonify(menu_collection.data)

