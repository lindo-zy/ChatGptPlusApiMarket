#!/usr/bin/python3
# -*- coding:utf-8 -*-

from fastapi import APIRouter

from chatgpt.db import db_session
from chatgpt.models.users import User
from chatgpt.schemas.services import RequestSchema
from chatgpt.utils.jwt_tool import JwtTool

app = APIRouter(prefix='/service')


@app.post('/request')
async def request(item: RequestSchema):
    """
    请求验证接口
    :param item:
    :return:
    """
    # 这个接口在api调用成功后再触发，否则api未访问成功也扣费，逻辑有问题
    try:
        info = JwtTool.check_access_token(item.jwt_token)
        if info:
            username = info['username']
            # 查询数据库剩余次数
            with db_session as session:
                rows = session.query(User).filter_by(username=username).with_for_update().limit(1).all()
                # 如果有这个用户，更新次数
                if rows:
                    remaining_count = rows[0].remaining_count
                    if remaining_count - 1 < 0:
                        return {'message': '用户剩余次数为0！', 'status': 'error'}
                    else:
                        rows[0].remaining_count -= 1
                        session.commit()
                        return {'message': 'request处理成功！', 'status': 'success'}
                else:
                    # 没有这个用户
                    return {'message': 'request接口异常！', 'status': 'error'}
        return {'message': 'request接口异常！', 'status': 'error'}
    except Exception as e:
        return {'message': f'request接口异常！{e}', 'status': 'error'}
