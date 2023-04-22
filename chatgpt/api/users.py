#!/usr/bin/python3
# -*- coding:utf-8 -*-

from fastapi import APIRouter

from chatgpt.db import db_session
from chatgpt.models.users import User
from chatgpt.schemas.users import RegisterVipSchema, LoginSchema, QuerySchema
from chatgpt.utils.jwt_tool import JwtTool

app = APIRouter(prefix='/user')


@app.post('/register_vip')
async def register_vip(item: RegisterVipSchema):
    """
    vip用户注册
    :return:
    """
    try:
        with db_session as session:
            rows = session.query(User).filter_by(username=item.username).with_for_update().all()
            # 如果有这个用户，那么就增加次数
            if rows:
                for row in rows:
                    row.remaining_count += item.remaining_count
            else:
                # 如果没有这个用户，则添加这个用户再增加次数
                new_object = User(username=item.username, remaining_count=item.remaining_count)
                session.add(new_object)
            session.commit()
        return {'message': f'付费用户:{item.username}添加成功', 'status': 'success'}
    except Exception as e:
        return {'message': f'register_vip接口异常：{e}', 'status': 'error'}


@app.post('/login')
async def login(item: LoginSchema):
    """
    vip登陆
    :param item:
    :return:
    """
    try:
        with db_session as session:
            rows = session.query(User).filter_by(username=item.username).all()
            if rows:
                username = rows[0].username
                remaining_count = rows[0].remaining_count
                # 返回一个jwt
                jwt = JwtTool.create_access_token(username=username, num=remaining_count)
                return {'message': f'付费用户:{item.username}登陆成功！', 'status': 'success', 'token': jwt}
            else:
                return {'message': f'付费用户:{item.username}不存在', 'status': 'error'}
    except Exception as e:
        return {'message': f'login接口异常：{e}', 'status': 'error'}


@app.post('/query')
async def query(item: QuerySchema):
    """
    查看当前jwt的剩余次数
    :param item:
    :return:
    """
    info = JwtTool.check_access_token(item.jwt_token)
    if info:
        username = info['username']
        with db_session as session:
            rows = session.query(User).filter_by(username=username).all()
            if rows:
                num = rows[0].remaining_count
                return {'message': '剩余次数查询成功！', 'num': num, 'status': 'success'}

    return {'message': '查询接口异常！', 'status': 'error'}
