#!/usr/bin/python3
# -*- coding:utf-8 -*-

from fastapi import APIRouter

from chatgpt.handle.token import token_manager
from chatgpt.schemas.services import RequestOpenaiSchema
from chatgpt.utils.jwt_tool import JwtTool

app = APIRouter(prefix='/service')


#
# prompt = "帮我写一个python的二叉树"
# import os
#
# os.environ['HTTP_PROXY'] = 'http://localhost:1081'
# os.environ['HTTPS_PROXY'] = 'http://localhost:1081'
#
#
# def use_api(prompt):
#     response = openai.ChatCompletion.create(
#         model='gpt-3.5-turbo',
#         message=[{'role': 'user',
#                   'content': prompt}]
#     )
#     return response['choice'][0]['message']['content']
#
#
# r = use_api(prompt)
# print(r)

# 用户通过这个接口调用真实的open api
# 1.限流，5s调用一次
# 2.每次调用时校验token和次数
# 3.


@app.post('/request_openai/')
async def request_openai(item: RequestOpenaiSchema):
    """
    使用token访问openapi接口
    :return:
    """
    if not JwtTool.check_access_token(item.token):
        return {'message': 'token异常！', 'status': 'error'}
    if not token_manager.verify_token(item.token):
        return {'message': 'token异常！', 'status': 'error'}
    try:
        # openai.api_key = settings.CHAT_GPT_API_KEY
        # prompt = item.prompt
        # response = openai.ChatCompletion.create(
        #     model='gpt-3.5-turbo',
        #     message=[{'role': 'user',
        #               'content': prompt}]
        #     # message=message
        # )
        # r = response['choice'][0]['message']['content']
        r = '123'
        return {'content': r, "message": 'gpt-3.5-turbo', 'status': 'success'}
    except Exception as e:
        print(e)
    return {'message': '接口访问异常', 'status': 'error'}
