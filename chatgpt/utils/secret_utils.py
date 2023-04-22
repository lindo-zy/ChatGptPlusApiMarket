#!/usr/bin/python3
# -*- coding:utf-8 -*-
import random


class SecretUtils:

    @staticmethod
    def gen_secret_key():
        """
        随机生成6位数
        (100000, 466665), (466666, 833331), (833332, 999999)
        :return:
        """
        normal_key = random.randint(100000, 466665)
        group_key = random.randint(466666, 833331)
        vip_key = random.randint(833332, 999999)
        return normal_key, group_key, vip_key
