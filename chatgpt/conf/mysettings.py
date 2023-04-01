#!/usr/bin/python3
# -*- coding:utf-8 -*-
from pydantic import BaseSettings


class MySettings(BaseSettings):
    SECRET_KEY: str = 'coda'
    ALGORITHM: str = 'HS256'
    # 60 minutes * 24 hours * 30 days = 30 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30
    # 1天过期
    NORMAL_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

    # 管理员的token配置
    ADMIN_TOKEN_LIST = ['CODA', 'coda', 'zy']
    # 免费次数配置
    # 白嫖次数
    NORMAL_NUM = 10
    # 加群增加的次数
    GROUP_NUM = 50
    # 加入星球的次数
    VIP_NUM = 10000

    # 数据库配置
    DATABASE = 'chatgpt'
    DB_HOST = '127.0.0.1'
    DB_USERNAME = 'ROOT'
    DB_PASSWORD = '123456'


settings = MySettings()
