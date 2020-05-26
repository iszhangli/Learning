# -*- coding:utf-8 -*-
# name: 1. 单链表 
# author: li zhang
# date: 2020/3/26

# 从交换变量
class Node(object):
    '''构建数据结构代表节点'''
    def __init__(self, val):
        self.val = val
        self.next = None

# 这是一个单链表，都是对它进行参数
class SingleLinkList(object):
    '''单链表'''

    def __init__(self, node=None):
        '''在这里面定义对象属性'''
        self.__head = node  # 头结点是node
        pass

    def is_empty(self):
        return self.__head is None

    def length(self):
        # 游标指向头部
        cursor = self.__head
        count = 0
        while cursor is not None:
            count += 1
            cursor = cursor.next
        return count

    def travel(self):
        cursor = self.__head
        while cursor is not None:
            print(cursor.val, end=' ')
            cursor = cursor.next

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head = node

    def append(self, item):
        '''在哪个节点上添加
        输入的是一个数据
        '''
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cursor = self.__head
            while cursor.next is not None:
                cursor = cursor.next
            cursor.next = node

    def insert(self, item):  # TODO
        """
        插入需要两个变量 一个是 val 和 index
        """
        node = Node(item)
        if self.is_empty():
            self.__head = node
        elif self.length() < item:
            print('the length')
            return 0
        else:
            # 1. 空
            # 2. 正常插入
            # 3. 长度不够
            cursor = self.__head
            for i in range(item-2):
                cursor = cursor.next
            node.next = cursor.next
            cursor.next = node


    def remove(self, item):
        pass

    def search(self, item):
        '''判断元素是否存在'''
        pass

# 构建一个列表需要
if __name__ == '__main__':

    single_l= SingleLinkList()
    print(single_l.is_empty())
    print(single_l.length())
    single_l.append(1)
    print(single_l.is_empty())
    print(single_l.length())
    single_l.append(2)
    single_l.append(3)
    single_l.append(4)
    single_l.append(8)
    print(single_l.travel())
    single_l.add(19)
    single_l.add(199)
    print(single_l.travel())