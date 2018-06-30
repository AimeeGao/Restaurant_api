"""
 Created by 七月 on 2018/5/1.
"""
__author__ = '七月'

from app import create_app
from app.api.persona.models.course import Course
from app.libs.model_base import db

app = create_app()
with app.app_context():
    with db.auto_commit():
        # 一门课程
        course1 = Course()
        course1.name = 'Flask 高级编程'
        course1.platform = 300
        course1.slogan = '信仰圣光吧'
        course1.thumbnail = 'img/one.jpg'
        db.session.add(course1)
        # 一门课程
        course2 = Course()
        course2.name = 'Flask API'
        course2.platform = 300
        course2.slogan = '构建一套适配 微信小程序/App/单页面 等前端的优秀RESTful API框架。'
        course2.thumbnail = 'img/two.jpg'
        db.session.add(course2)

#
# {
#        "name": "Flask 高级编程",
#        "platform": "慕课",
#        "slogan": "信仰圣光吧",
#        "thumbnail": "http://77.art:5000/static/img/one.jpg",
#        "verify": "已验证"
#    }
