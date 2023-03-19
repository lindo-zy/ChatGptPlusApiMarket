#!/usr/bin/python3
# -*- coding:utf-8 -*-

from pydantic import BaseModel


class RequestOpenaiSchema(BaseModel):
    token: str
    prompt: str
