#!/usr/bin/python3
# -*- coding:utf-8 -*-
from fastapi import APIRouter

from chatgpt.api import items
from chatgpt.api import services
from chatgpt.api import users

api_router = APIRouter()
api_router.include_router(items.app, tags=['items'])
api_router.include_router(users.app, tags=['users'])
api_router.include_router(services.app, tags=['services'])


@api_router.get('/')
def index():
    return '项目启动成功！'


@api_router.on_event("startup")
async def startup_event():
    """
    启动前的钩子
    :return:
    """
    # 1.
