#!/usr/bin/python3
# -*- coding:utf-8 -*-

from pydantic import BaseModel


class VerifySchema(BaseModel):
    token: str
