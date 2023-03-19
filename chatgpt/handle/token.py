#!/usr/bin/python3
# -*- coding:utf-8 -*-
import json
import os
import os.path
from typing import Dict

from chatgpt.utils.file_utils import FileUtils
from chatgpt.utils.jwt_tool import JwtTool


class TokenManager:
    """
    token管理
    """

    def __init__(self):
        self.path = os.path.join(os.getcwd(), 'market')
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        # 记录当前所有的token
        self.json_path = os.path.join(self.path, 'token.json')

    def gen_token_by_times(self, username: str, times: int) -> Dict[str, int]:
        """
        生成按次计算的token
        :param username:
        :param times:
        :return:
        """
        # 1.生成token写入到对应的json文件管理
        # 2.写入到token.json进行管理,后续用于验证这个token
        token = JwtTool.create_access_token(username)
        result = {token: times}
        file_path = os.path.join(self.path, f'{username}.json')
        FileUtils.write_json_file(file_path, json.dumps(result))
        self._add_token(token)
        return result

    def gen_token_by_day(self) -> str:
        """
        生成按天计算的token,即为原生JWT
        :return:
        """
        pass

    def delete_token(self, token: str) -> bool:
        """
        删除指定token
        :return:
        """
        # 1.删除对应的json文件
        # 2.删除token.json里面的值
        try:
            result = JwtTool.check_access_token(token)
            username = result.get('sub')
            file_path = os.path.join(self.path, f'{username}.json')
            FileUtils.remove_json_file(file_path)
            data = FileUtils.read_json_file(self.json_path)
            if isinstance(data, list):
                if token in data:
                    data.remove(token)
            FileUtils.write_json_file(self.json_path, json.dumps(data))
            return True
        except Exception as e:
            print(e)
        return False

    def query_token(self, username: str) -> str:
        """
        查询token
        :return:
        """
        file_path = os.path.join(self.path, f'{username}.json')
        return FileUtils.read_json_file(file_path)

    def _add_token(self, token: str):
        """
        添加token到token.json
        :return:
        """
        data = FileUtils.read_json_file(self.json_path)
        if isinstance(data, list):
            data.append(token)
        FileUtils.write_json_file(self.json_path, json.dumps(data))

    def verify_token(self, token: str):
        """
        使用token
        :param token:
        :return:
        """
        data = FileUtils.read_json_file(self.json_path)
        if token not in data:
            return False
        return True

    def user_token(self, token: str):
        """
        使用token，使用后次数-1,为0后删除指定token
        :param username:
        :return:
        """
        result = JwtTool.check_access_token(token)
        username = result.get('sub')
        file_path = os.path.join(self.path, f'{username}.json')
        token_data = FileUtils.read_json_file(file_path)
        times = token_data[token]
        times -= 1
        if times <= 0:
            self.delete_token(token)
        else:

            FileUtils.write_json_file(file_path, json.dumps({token: times}))


token_manager = TokenManager()
