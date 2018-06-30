"""
 Created by 七月 on 2018/6/2. @林间有风
"""
# from app.api.restaurant.models.course import Course
# from app.api.restaurant.models.dev_key import CourseDevKey
# from app.api.restaurant.models.legal import Legal
# from app.api.restaurant.models.user import User
# from app.libs.enums import ClientTypeEnum
# from app.libs.error_code import Success, ImoocBuyerVerifyException, CourseNotExistException
# from app.libs.helper import get_random_str
# from app.libs.model_base import db
# from app.libs.redis import redis
# from app.libs.redprint import Redprint
# from app.validators.forms import ClientForm, DeveloperImoocForm
# from app.libs.token_auth import auth
# from flask import jsonify, g

# __author__ = '七月'

# api = Redprint('dev')


# @api.route('/appkey', methods=['POST'])
# @auth.login_required
# def get_appkey():
#     """
#     生成 appkey
#     校验
#     ---
#     parameters:
#       - name: account
#         in: body
#         type: int
#         required: true
#         example: 115
#     responses:
#       200:
#         description: 返回信息
#         examples:
#           success : {"appkey": "hNbUdRkaktlc9Db6"}
#     """
#     form = ClientForm().validate_for_api()
#     promise = {
#         ClientTypeEnum.DEVELOPER_IMOOC: __generate_imooc_appkey
#     }
#     key = promise[form.type.data]()
#     return jsonify({
#         'appkey': key
#     }), 201


# @api.route('/verify', methods=['POST'])
# @auth.login_required
# def verify_imooc_buyer():
#     """
#     验证用户是否购买课程
#     校验
#     ---
#     parameters:
#       - name: cid
#         type: int
#         required: true
#         example: 124
#     responses:
#       200:
#         description: 返回信息
#         examples:
#           success : { "error_code": 0,"msg": "ok","request": "POST /restaurant/v1/dev/verify"}
#     """
#     # 登录后
#     # 验证uid,cid,key
#     form = ClientForm().validate_for_api()
#     promise = {
#         ClientTypeEnum.DEVELOPER_IMOOC: __verify_buyer_imooc
#     }
#     if promise[form.type.data]():
#         return Success()
#     return ImoocBuyerVerifyException()


# @api.route('/appkey/<app_key>', methods=['PUT'])
# @auth.login_required
# def change_app_key(app_key):
#     uid = g.user.uid
#     with db.auto_commit():
#         dev_key = CourseDevKey.query.filter_by(
#             key=app_key, activate=1, uid=uid).first_or_404()
#         dev_key.key = get_random_str(16)
#     redis.connection.delete(app_key)
#     redis.connection.set(dev_key.key, uid)
#     return jsonify({
#         'appkey': dev_key.key
#     }), 201


# def __verify_buyer_imooc():
#     """
#         这里可以拿到cid和uid
#         通过这两个参数，加上七月的唯一标识调用慕课服务可以验证
#         慕课用户是否购买某个课程
#         目前，请先忽略验证，直接返回一个开发者key
#         ---
#     """
#     form = DeveloperImoocForm().validate_for_api()
#     # 慕课网课程id
#     cid = form.cid.data
#     muid = form.account.data
#     # 校验是否购买课程
#     __check_imooc(muid, cid)

#     uid = g.user.uid
#     # 判断user表中是否已经存在muid的用户
#     # 此时已经判断用户购买了慕课网课程
#     # 检查该用户是否已经验证过其它课程，如果没有验证则添加muid字段
#     User.check_muid(muid, uid)
#     # create 此时已判断用户（uid）已经购买了课程（cid），并将其写入Legal表中
#     __create_one_legal(cid, uid)
#     return True


# def __generate_imooc_appkey():
#     """
#         发放开发者appkey，需要先验证是否购买课程
#         appkey使用16位随机字符串，尽可能保证不重复如果验证不通过需要返回具体错误消息
#         ---
#     """
#     # 首先查询legal，是否有记录，如果没有说明验证没有通过
#     # 如果有记录，那么创建key，保存key，并返回

#     # TODO
#     form = DeveloperImoocForm().validate_for_api()
#     # cid为其它课程平台的id
#     # 需转换为本系统的课程id
#     pcid = form.cid.data
#     course = Course.query.filter_by(pcid=pcid).first()
#     if not course:
#         raise CourseNotExistException()
#     # muid = form.account.data
#     uid = g.user.uid
#     cid = course.id
#     Legal.verify(uid, cid)
#     # Legal中已经存在响应的购买关系，发放appkey
#     # 注册到数据库中
#     app_key = CourseDevKey.create_key(uid, cid)
#     redis.connection.set(app_key, uid)
#     return app_key


# # 生成数据
# def __create_one_legal(cid, uid):
#     # 根据pcid查找本系统的课程id
#     # 此时用户已经登录成功
#     course = Course.query.filter_by(pcid=cid).first()
#     if course:
#         with db.auto_commit():
#             legal = Legal()
#             # legal.cid = cid
#             # 写入到legal表中的为本系统的课程id号
#             legal.cid = course.id
#             legal.uid = uid
#             db.session.add(legal)
#     else:
#         raise CourseNotExistException()


# def __check_imooc(muid, cid):
#     from app.libs.dangerous import check_immoc_buyer
#     if not check_immoc_buyer(muid=muid, cid=cid):
#         raise ImoocBuyerVerifyException()
