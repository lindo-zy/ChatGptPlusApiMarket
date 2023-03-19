#!/usr/bin/python3
# -*- coding:utf-8 -*-
import json
import shutil


class FileUtils:
    @staticmethod
    def write_json_file(json_path: str, content: str):
        try:
            with open(json_path, r'w+', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(e)

    @staticmethod
    def read_json_file(json_path: str):
        try:
            with open(json_path, r'r+', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(e)

    @staticmethod
    def remove_json_file(json_path: str):
        try:
            shutil.rmtree(json_path)
        except Exception as e:
            print(e)
