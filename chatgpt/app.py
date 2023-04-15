#!/usr/bin/python3
# -*- coding:utf-8 -*-
from datetime import datetime, timedelta
from typing import Dict

from fastapi import FastAPI, Request, HTTPException
from starlette.middleware.cors import CORSMiddleware

from chatgpt.core.router import api_router

# 存储IP地址和最近一次访问时间的字典
ip_access_time: Dict[str, datetime] = {}

def creat_app():
    # 在线部署时，关闭docs_url
    app = FastAPI()
    # 添加中间件，处理跨域问题
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.middleware("http")
    async def rate_limit(request: Request, call_next):
        # 获取请求的IP地址
        client_host = request.client.host

        # 如果IP地址已经存在于字典中，检查是否满足0.5秒内只能访问一次的限制
        if client_host in ip_access_time and client_host not in ['127.0.0.1']:
            last_access_time = ip_access_time[client_host]
            time_since_last_access = datetime.now() - last_access_time
            if time_since_last_access < timedelta(seconds=0.5):
                raise HTTPException(status_code=429, detail="Too many requests")

        # 更新IP地址的最近一次访问时间，并将其加入字典
        ip_access_time[client_host] = datetime.now()

        # 继续处理请求
        response = await call_next(request)
        return response

    # 添加路由
    app.include_router(api_router)
    return app
