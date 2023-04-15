#!/usr/bin/python3
# -*- coding:utf-8 -*-
import os

from dotenv import load_dotenv
from pydantic import BaseSettings

# 加载.env文件中的环境变量
load_dotenv('.env')


class MySettings(BaseSettings):
    SECRET_KEY: str = 'chatgpt1'
    ALGORITHM: str = 'HS256'
    # 60 minutes * 24 hours * 30 days = 30 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30
    # 1天过期
    NORMAL_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

    # 管理员的token配置
    ADMIN_TOKEN_LIST = ['coda', 'zy']
    # 免费次数配置
    # 白嫖次数
    NORMAL_NUM = 10
    # 加群增加的次数
    GROUP_NUM = 50
    # 加入星球的次数
    VIP_NUM = 100

    # 数据库配置
    DATABASE = 'chatgpt'
    DB_HOST = '127.0.0.1'
    DB_USERNAME = 'root'
    # DB_PASSWORD = '123456'
    DB_PASSWORD = 'P@ssw0rd'

    # openai的秘钥
    OPENAI_API_KEY = '123'
    # 后台每日最大访问次数
    MAX_REQUEST = 10000

    # 微信号
    WEIXIN_CODE = os.getenv('WEIXIN_CODE')


settings = MySettings()
