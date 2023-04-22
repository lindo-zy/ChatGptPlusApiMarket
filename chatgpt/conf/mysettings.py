#!/usr/bin/python3
# -*- coding:utf-8 -*-
import os

from dotenv import load_dotenv
from pydantic import BaseSettings

# 加载.env文件中的环境变量
if not load_dotenv('.dev.env'):
    load_dotenv('.env')


class MySettings(BaseSettings):
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM: str = os.getenv('ALGORITHM')

    # 60 minutes * 24 hours * 30 days = 30 days
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    # 1天过期
    NORMAL_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

    # 管理员的token配置
    ADMIN_TOKEN_LIST: str = os.getenv("ADMIN_TOKEN_LIST")
    # 免费次数配置
    # 白嫖次数
    NORMAL_NUM: int = os.getenv("NORMAL_NUM")
    # 加群增加的次数
    GROUP_NUM: int = os.getenv("GROUP_NUM")
    # 加入星球的次数
    VIP_NUM: int = os.getenv("VIP_NUM")

    # 数据库配置
    DATABASE: str = os.getenv("DATABASE")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_USERNAME: str = os.getenv("DB_USERNAME")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")

    # 后台每日最大访问次数
    MAX_REQUEST: int = os.getenv("MAX_REQUEST")

    # 微信号
    WEIXIN_CODE: str = os.getenv('WEIXIN_CODE')


settings = MySettings()
