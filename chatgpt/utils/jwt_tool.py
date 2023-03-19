#!/usr/bin/python3
# -*- coding:utf-8 -*-

from datetime import datetime, timedelta
from typing import Any, Union

import jwt

from chatgpt.conf.mysettings import settings


class JwtTool:
    """
    JWT工具类
    """

    @staticmethod
    def create_access_token(
            subject: Union[str, Any], expires_delta: timedelta = None
    ) -> str:
        """
        生成jwt
        :param subject:用户账号，可以用微信号生成
        :param expires_delta:默认一个月有效
        :return:
        """
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(
                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
            )
        to_encode = {"exp": expire, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt

    @staticmethod
    def check_access_token(jwt_token: str) -> dict:
        """
        验证token
        :param jwt_token:
        :return:
        """
        try:
            decoded_token = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
            return decoded_token
        except jwt.ExpiredSignatureError:
            print("Token has expired")
        except jwt.InvalidTokenError:
            print("Invalid token")
        except Exception as e:
            print(e)
        return {}


if __name__ == '__main__':
    print(JwtTool.create_access_token('123'))

    print(JwtTool.check_access_token(
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODE4MDkzNzYsInN1YiI6IjEyMyJ9.aRASzLH1Gk4nTtizQE5C_pZ7lCU9yPcTCk-_C2p8TfE'))
