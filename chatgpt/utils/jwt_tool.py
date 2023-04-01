#!/usr/bin/python3
# -*- coding:utf-8 -*-

from datetime import datetime, timedelta

import jwt

from chatgpt.conf.mysettings import settings


class JwtTool:
    """
    JWT工具类
    """

    @staticmethod
    def create_access_token(
            username: str,
            num: int
    ) -> str:

        """
        生成jwt,免费用户的jwt有效时间为1天，付费用户30天
        :param num:
        :param username: 用户名
        :return:
            """
        # 创建表示当前日期的datetime对象
        today = datetime.today()
        # 格式化日期并输出
        cur_date = today.strftime("date:'%Y-%m-%d'")
        if len(username) == 32:
            expire = datetime.utcnow() + timedelta(
                minutes=settings.NORMAL_ACCESS_TOKEN_EXPIRE_MINUTES
            )
        else:
            expire = datetime.utcnow() + timedelta(
                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
            )
        to_encode = {"exp": expire, "username": username, 'num': str(num), 'date': cur_date}
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
    pass
