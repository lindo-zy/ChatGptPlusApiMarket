#!/usr/bin/python3
# -*- coding:utf-8 -*-
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from chatgpt.core.router import APIRouter


def creat_app():
    app = FastAPI()
    # 添加中间件，处理跨域问题
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    router = APIRouter()
    app.include_router(router)
    return app
