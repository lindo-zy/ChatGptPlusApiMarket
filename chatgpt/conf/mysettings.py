#!/usr/bin/python3
# -*- coding:utf-8 -*-
from pydantic import BaseSettings


class MySettings(BaseSettings):
    SECRET_KEY: str = 'coda'
    ALGORITHM: str = 'HS256'
    # 60 minutes * 24 hours * 30 days = 30 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30

    # chatgpt的api，后面写成配置文件使用，最好简单编码下
    CHAT_GPT_API_KEY = ''
    # 管理员的token配置
    ADMIN_TOKEN_LIST = ['CODA', 'coda']


settings = MySettings()
