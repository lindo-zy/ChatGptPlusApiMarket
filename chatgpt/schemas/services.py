#!/usr/bin/python3
# -*- coding:utf-8 -*-

from pydantic import BaseModel


class RequestSchema(BaseModel):
    # jwt验证
    jwt_token: str
