#!/usr/bin/python3
# -*- coding:utf-8 -*-

# api服务
import openai

openai.api_key = "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"

prompt = "帮我写一个python的二叉树"
import os

os.environ['HTTP_PROXY'] = 'http://localhost:1081'
os.environ['HTTPS_PROXY'] = 'http://localhost:1081'


def use_api(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        message=[{'role': 'user',
                  'content': prompt}]
    )
    return response['choice'][0]['message']['content']


r = use_api(prompt)
print(r)

# 用户通过这个接口调用真实的open api
# 1.限流，5s调用一次
# 2.每次调用时校验token和次数
# 3.
