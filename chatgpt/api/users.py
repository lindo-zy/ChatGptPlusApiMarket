#!/usr/bin/python3
# -*- coding:utf-8 -*-
import random
import uuid

from fastapi import APIRouter

from chatgpt.conf.mysettings import settings
from chatgpt.db import db_session
from chatgpt.models.users import User, SecretKey
from chatgpt.schemas.users import RegisterVipSchema, LoginSchema, QuerySchema, VerifySchema, GenKeySchema
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


@app.post('/verify')
async def verify(item: VerifySchema):
    """
    验证当前key是否有效
    :param item:
    :return:
    """
    # 当前白嫖用户使用秘钥进行验证，更新换秘钥重新生成jwt即可
    try:
        with db_session as session:
            rows = session.query(SecretKey).all()
            normal_key = rows[0].normal_key
            # 2类key,微信群的key
            group_key = rows[0].group_key
            # 3类key,星球的key
            vip_key = rows[0].vip_key
            if item.secret_key in [normal_key, str(normal_key), group_key, str(group_key), vip_key, str(vip_key)]:
                num_map = {
                    str(normal_key): settings.NORMAL_NUM,
                    str(group_key): settings.GROUP_NUM,
                    str(vip_key): settings.VIP_NUM,
                }
                cur_num = num_map[item.secret_key]
                username = uuid.uuid4()
                # 写入到数据库
                rows = session.query(User).filter_by(username=username).with_for_update().all()
                if not rows:
                    new_object = User(username=username, remaining_count=cur_num)
                    session.add(new_object)
                    session.commit()
                jwt = JwtTool.create_access_token(username=str(username), num=cur_num)
                return {'message': f'免费用户:{username}添加成功', 'status': 'success', 'token': jwt}
            else:
                return {'message': "非法秘钥！", 'status': 'error'}
    except Exception as e:
        return {'message': f'verify接口异常：{e}', 'status': 'error'}


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


@app.post('/gen_key')
async def gen_key(item: GenKeySchema):
    """
    更新秘钥
    :param item:
    :return:
    """
    if item.admin_token in settings.ADMIN_TOKEN_LIST:
        # 更新数据库中的秘钥
        with db_session as session:
            rows = session.query(SecretKey).with_for_update().limit(1).all()
            # 随机生成6位数
            # (100000, 466665), (466666, 833331), (833332, 999999)
            normal_key = random.randint(100000, 466665)
            group_key = random.randint(466666, 833331)
            vip_key = random.randint(833332, 999999)
            for row in rows:
                row.normal_key = normal_key
                row.group_key = group_key
                row.vip_key = vip_key
            session.commit()
            return {'message': '秘钥更新完成！', 'status': 'success', 'normal_key': normal_key, 'group_key': group_key,
                    'vip_key': vip_key}

    return {'message': '无效的秘钥！', 'status': 'error'}
