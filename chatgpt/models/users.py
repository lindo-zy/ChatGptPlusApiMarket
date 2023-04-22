#!/usr/bin/python3
# -*- coding:utf-8 -*-

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from chatgpt.utils.secret_utils import SecretUtils

Base = declarative_base()
normal_key, group_key, vip_key = SecretUtils.gen_secret_key()


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
    normal_key = Column(String(255), nullable=False, default=str(normal_key))
    # 2类key,微信群的key
    group_key = Column(String(255), nullable=False, default=str(group_key))
    # 3类key,星球的key
    vip_key = Column(String(255), nullable=False, default=str(vip_key))
    # 管理员秘钥
    # admin_key = Column(String(255), nullable=False, default='nemo666')


class Counter(Base):
    """
    统计次数
    """
    __tablename__ = 'counter'
    # 自增id
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 次数
    count = Column(Integer, nullable=False)
