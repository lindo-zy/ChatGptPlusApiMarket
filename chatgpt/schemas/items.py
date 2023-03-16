#!/usr/bin/python3
# -*- coding:utf-8 -*-
from pydantic import BaseModel


class GenApiSchema(BaseModel):
    # 管理员的token
    token: str
