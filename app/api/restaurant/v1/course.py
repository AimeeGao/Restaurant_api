"""
 Created by 七月 on 2018/6/7. @林间有风
"""
# from app.api.restaurant.models.course import Course
# from app.api.restaurant.models.legal import Legal
# from app.api.restaurant.view_model.course import CourseCollection
# from app.libs.redprint import Redprint
# from flask import jsonify, g
# from sqlalchemy import desc

# from app.libs.token_auth import auth

# __author__ = '七月'

# api = Redprint('course')


# @api.route('', methods=['GET'])
# @auth.login_required
# def get_courses():
#     """
#     获得课程列表
#     全部课程
#     ---
#     responses:
#       200:
#         description: 返回信息
#         examples:
#           success : { "thumbnail": "http://77.art:5000/img/one.jpg","create_time": 1528450392,"id": 1,"name": "Flask 高级编程","platform": 300,"slogan": "信仰圣光吧","status": 1}
#     """
#     # TODO 获取课程列表
#     # 为测试方便，目前不做超权检测，uid号显式传递，后面需要更改为从
#     # g变量中获取
#     uid = g.user.uid
#     course_list = Course.query.filter_by(status=1).order_by(desc(Course.create_time)).all()
#     legals_of_mine = Legal.query.filter_by(uid=uid).all()
#     course_collection = CourseCollection(course_list, legals_of_mine)
#     return jsonify(course_collection.data)

# # https://coding.imooc.com/class/220.html
