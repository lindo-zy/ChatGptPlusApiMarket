#!/usr/bin/python3
# -*- coding:utf-8 -*-
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = 'secret_key'
    ALGORITHM: str = 'HS256'
    # 60 minutes * 24 hours * 30 days = 30 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30

    # chatgpt的api，后面写成配置文件使用，最好简单编码下
    CHAT_GPT_API_KEY = ''
    # 生成的链接地址


settings = Settings()
