# !/usr/bin/env python# -*- coding:utf-8 -*-# name: 02_小试牛刀 # author: li zhang# date: 2019/12/3def deco(func):    def inner():        print('->: run inner()')    return inner()@decodef target():    print('->: run target()')# target() # 实际上只是证明target=deco(target) 并没有调用其他实质性的操作# 什么是装饰器# @+函数名，其修饰一个函数，参数就是被修饰的这个函数# 有什么作用# 增强函数的行为registry = []def register(func):    print('running register(%s)' % func)    registry.append(func)    return func@registerdef f1():    print('running f1()')@registerdef f2():    print('running f2()')def f3():    print('running f3()')def main():    print('running main()')    print('registry: ', registry)    f1()    f2()    f3()if __name__ == '__main__':    main()# 函数装饰器在被导入模块时立即运行（装饰几个函数就运行几次），而被装饰的函数只有在调用时才运行# 经常遇到的情况，装饰器在其他模块中定义会怎么样