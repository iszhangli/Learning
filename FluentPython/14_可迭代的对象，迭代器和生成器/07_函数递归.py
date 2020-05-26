# -*- coding:utf-8 -*-
# author: li zhang
# date: 2020/3/31 13:38

def mul(n):
    if n == 1:
        return 1

    return n*mul(n-1)

