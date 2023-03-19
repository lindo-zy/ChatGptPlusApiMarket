#!/usr/bin/python3
# -*- coding:utf-8 -*-
from pydantic import BaseModel


class GenTokenSchema(BaseModel):
    # 管理员的token
    admin_token: str
    # 生成token使用的用户名
    username: str
    # 生成的次数
    times: int


class DeleteTokenSchema(BaseModel):
    # 管理员的token
    admin_token: str
    # 待删除的token
    token: str
