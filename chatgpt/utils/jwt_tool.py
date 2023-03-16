#!/usr/bin/python3
# -*- coding:utf-8 -*-

from datetime import datetime, timedelta
from typing import Any, Union

import jwt

from chatgpt.conf.settings import settings


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
        :param subject:
        :param expires_delta:
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
    def check_access_token(jwt_token: str) -> bool:
        """
        验证token
        :param jwt_token:
        :return:
        """
        try:
            decoded_token = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
            print(decoded_token)
            return True
        except jwt.ExpiredSignatureError:
            print("Token has expired")
        except jwt.InvalidTokenError:
            print("Invalid token")
        except Exception as e:
            print(e)
        return False


if __name__ == '__main__':
    # print(JwtVerify.create_access_token('123'))

    print(JwtTool.check_access_token(
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODE1NjU0MDksInN1YiI6IjEyMyJ9.LlP7LrRMsMGTRy_N-mQC1XEzdooU2iJ9Qad8HKOopcI'))
