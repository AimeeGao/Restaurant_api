"""
 Created by 七月 on 2018/6/2.
"""
from flask import render_template

from app.libs.redprint import Redprint

__author__ = '七月'

web = Redprint('index', with_prefix=False)


@web.route('/')
def index():
    return render_template('index.html')
