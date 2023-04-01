#!/usr/bin/python3
# -*- coding:utf-8 -*-
from fastapi import APIRouter

from chatgpt.api import services, users, items
from chatgpt.db import create_all

api_router = APIRouter()
api_router.include_router(services.app, tags=['services'])
api_router.include_router(items.app, tags=['items'])
api_router.include_router(users.app, tags=['users'])


@api_router.get('/')
def index():
    return '项目启动成功！'


@api_router.on_event("startup")
async def startup_event():
    """
    启动前的钩子
    :return:
    """
    create_all()
