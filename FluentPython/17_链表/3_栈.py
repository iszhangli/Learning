# -*- coding:utf-8 -*-
# author: li zhang
# date: 2020/4/1 10:30

class Stack(object):

    def __init__(self, l=[]):
        self.__list = l

    def push(self, item):
        self.__list.append(item)

    def pop(self, item):
        self.__list.pop()

    def peak(self):
        '''返回栈顶元素'''
        if self.__list == []:
            return None
        return self.__list[-1]

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)

def main():
    s = Stack()

if __name__ == '__main__':
    main()