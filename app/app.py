"""
 Created by 七月 on 2018/5/7.
"""
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
import json

from app.libs.error_code import ServerError
from datetime import date
import decimal

__author__ = '七月'



class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        # 定义decimal类型的序列化方法
        if isinstance(o,decimal.Decimal):
            return  "%.2f" % o
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder



