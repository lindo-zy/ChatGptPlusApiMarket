#!/usr/bin/python3
# -*- coding:utf-8 -*-
from fastapi import APIRouter

from chatgpt.schemas.items import GenApiSchema

app = APIRouter(prefix='/items')


# 管理员 api生成
@app.post('/gen_api/')
async def gen_api(item: GenApiSchema):
    """
    生成api链接
    :return:
    """
    # 检查是否为有效token
    if item not in ['']:
        return
