#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Create time : 2020/7/30 16:26
@Author      : zhang li
@Version     : 1.0
'''

# Here put the import lib

# Definition for singly-linked list.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def getKthFromEnd(head, k):
    if head is None:
        return

    else:
        cursor = head
        len = 1
        while cursor.next is not None:
            cursor = cursor.next
            len += 1

        n = len-k
        cursor = head
        while n>0:
            cursor = cursor.next
            n = n-1
        return head.val

        n = len-k
        cursor = head
        len = 1
        while cursor.next is not None:
            cursor = cursor.next
            len += 1
            if n == len:
                return cursor

def kthToLast(head, k):
    a = head
    b = head
    for i in range(k):
        b = b.next
    while b:
        a = a.next
        b = b.next
    return a.val


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


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 7, 6, 4, 9]
    sing = SingalList()
    for i in l:
        sing.append(i)
    kthToLast(sing.head, 3)


