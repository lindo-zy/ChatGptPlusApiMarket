#!/usr/bin/python3
# -*- coding:utf-8 -*-


from fastapi import APIRouter

from chatgpt.conf.mysettings import settings
from chatgpt.handle.token import token_manager
from chatgpt.schemas.users import GenTokenSchema, DeleteTokenSchema

app = APIRouter(prefix='/user')


@app.post('/gen_token/')
async def gen_token(item: GenTokenSchema):
    """
    生成token,仅管理员
    :return:
    """
    if item.admin_token not in settings.ADMIN_TOKEN_LIST:
        return {'message': '管理员身份验证异常！', 'status': 'error'}
    data = token_manager.gen_token_by_times(item.username, item.times)
    return {'message': 'token生成完成！', 'token': data.get('token'), 'status': 'success'}


@app.get('/token/{username}')
async def token(username: str):
    """
    查看指定token
    :return:
    """
    return token_manager.query_token(username)


@app.post('/delete_token/')
async def delete_token(item: DeleteTokenSchema):
    """
    删除token,仅管理员
    :return:
    """
    if item.admin_token not in settings.ADMIN_TOKEN_LIST:
        return {'message': '管理员身份验证异常！', 'status': 'error'}
    flag = token_manager.delete_token(item.token)
    return {'message': f'token删除：{flag}', 'status': 'success'}
