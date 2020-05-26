# -*- coding:utf-8 -*-
# author: li zhang
# date: 2020/3/30 10:03

# 多任务 有多个函数一块跑
# 没有多任务的程序
import time
import threading

def sing():
    for i in range(5):
        # time.sleep(1)
        print('sing sing')


def dance():
    for i in range(5):
        # time.sleep(1)
        print('dance dance')


def main():
    t1 = threading.Thread(target=sing)  #
    t2 = threading.Thread(target=dance)
    t1.start()
    time.sleep(1)
    t2.start()

    while True:
        length = len(threading.enumerate())
        print('length: ', length)
        print(threading.enumerate())
        if length <= 1:
            break

if __name__ == '__main__':
    main()