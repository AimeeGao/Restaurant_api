"""
 Created by 七月 on 2018/6/2.
"""
from flask import Blueprint
from app.web import index

__author__ = '七月'


def create_blueprint_web():
    bp_web = Blueprint('web', __name__, template_folder='templates',
                       static_folder='static')

    index.web.register(bp_web)
    return bp_web
