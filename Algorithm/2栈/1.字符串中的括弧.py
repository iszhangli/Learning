#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Create time : 2020/7/27 11:20
@Author      : zhang li
@Version     : 1.0
'''

# Here put the import lib

def scoreOfParentheses(S):
    stack = [0]

    for i in S:
        if i == '(':
            stack.append(0)
        else:
            v = stack.pop()
            stack[-1] += max(2*v, 1)
    return stack[0]


if __name__ == '__main__':
    s = '(()(()))'
    sorce = scoreOfParentheses(s)
    print(sorce)