# !/usr/bin/env python# -*- coding:utf-8 -*-# name: 06_叠放装饰器 # author: li zhang# date: 2019/12/3# 叠放装饰器按照顺序# d1(d2(func))# -----  这就是一个简单的装饰器def print_de(func):    print('i am a decator')    def wrapper(*args):        func(*args)    return wrapper@print_dedef multi(maxnum):    count = 1    for i in range(2, maxnum):        count = count * i    print(count)multi(10)