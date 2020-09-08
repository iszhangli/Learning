#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Create time : 2020/8/12 10:14
@Author      : zhang li
@Version     : 1.0
'''

# Here put the import lib


def logger(func):
    def wrapper(*args, **kw):
        print('Ready to run {}:'.format(func.__name__))

        func(*args, **kw)
        print('Function done!')
    return wrapper

@logger
def add(x, y):
    print('{} + {} = {}'.format(x, y, x + y))

if __name__ == '__main__':
    add(10, 29)