#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Create time : 2020/8/3 16:16
@Author      : zhang li
@Version     : 1.0
'''

# Here put the import lib

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

'''
输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
'''
def partition(head, x):
    left = left_head = Node(0)
    # left_head = Node(0)
    right = right_head = Node(0)
    # right_head = Node(0)

    while head:

        if head.val < x:
            left.next = head
            left = left.next

        else:
            right.next = head
            right = right.next

        head = head.next

    right.next = None
    left.next = right_head.next

    return left_head.next





if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 7, 6, 4, 9]
    sing = SingalList()
    for i in l:
        sing.append(i)

    partition(sing.head, 3)
