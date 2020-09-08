#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Create time : 2020/8/13 9:03
@Author      : zhang li
@Version     : 1.0
'''

# Here put the import lib
def deco(func):
    print("running register(%s)" % func)  # 添加该行
    def inner(*args):
        print('Running inner(), parameter is {}'.format((args)))
        func(args)  # 添加该行
    return inner

@deco
def target(n):
    print('Running target(), parameter is {}'.format(n))

if __name__ == '__main__':
    print('Running main()')
    target(9)