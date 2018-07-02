from sqlalchemy import Column, String, Integer, Boolean, Numeric, Float
from flask import url_for
from app.libs.model_base import Base, MixinModelJSONSerializer


# 菜单信息
class Menu(Base, MixinModelJSONSerializer):
    __bind_key__ = 'restaurant'
    id = Column(Integer, primary_key=True)
    name = Column(String(24), unique=True, nullable=False)
    price = Column(Float(10,2), nullable=False)
    description = Column(String(256))
    num = Column(Integer)
    #_img = Column('img', String(64))

# 将用户点的菜添加到菜单列表中 (GET)


# 获取添加数据后的菜单列表 (GET)
