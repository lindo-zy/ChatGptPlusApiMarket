#!/usr/bin/python3
# -*- coding:utf-8 -*-
from pydantic import BaseModel


class RegisterVipSchema(BaseModel):
    # 管理员的token
    admin_token: str
    # 生成token使用的用户名
    username: str
    # 生成的次数
    remaining_count: int


class LoginSchema(BaseModel):
    """
    使用用户登陆的为VIP用户
    """
    # 用户名
    username: str


class VerifySchema(BaseModel):
    # 秘钥
    secret_key: str


class QuerySchema(BaseModel):
    # jwt
    jwt_token: str


class GenKeySchema(BaseModel):
    # 管理员秘钥
    admin_token: str


class NodeToken(BaseModel):
    token: str
