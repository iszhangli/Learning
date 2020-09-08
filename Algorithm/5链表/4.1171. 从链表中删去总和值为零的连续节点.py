#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Create time : 2020/8/6 16:35
@Author      : zhang li
@Version     : 1.0
'''

# Here put the import lib
# https://leetcode-cn.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class SingalList():
    def __init__(self):
        self.head = None
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            cursor = self.head
            while cursor.next is not None:
                cursor = cursor.next
            cursor.next = node

def removeZeroSumSublists(head):
    pass

if __name__ == '__main__':
    l = [1,2,3,-3,-2]
    sing = SingalList()
    for i in l:
        sing.append(i)