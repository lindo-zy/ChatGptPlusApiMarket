#!/usr/bin/python3
# -*- coding:utf-8 -*-

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    用户表
    """
    __tablename__ = 'user'
    # 自增id
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    # 邮箱为vip客户，36位uuid4为普通用户
    username = Column(String(255), nullable=False)
    # 剩余次数
    remaining_count = Column(Integer, nullable=False)


class SecretKey(Base):
    """
    秘钥表
    """
    __tablename__ = 'secret_key'
    # 自增id
    key_id = Column(Integer, primary_key=True, autoincrement=True)
    # 1类key,关注公众号
    normal_key = Column(String(255), nullable=False)
    # 2类key,微信群的key
    group_key = Column(String(255), nullable=False)
    # 3类key,星球的key
    vip_key = Column(String(255), nullable=False)
