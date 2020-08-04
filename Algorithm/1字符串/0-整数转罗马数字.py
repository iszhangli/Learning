#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Create time : 2020/7/24 17:19
@Author      : zhang li
@Version     : 1.0
'''

# Here put the import lib

'''
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''
# 1-3999
'''
10 x
19 
'''
def intToRoman(num):
    dic = {1000:'M', 900:'CM', 500:'D', 400:'CD',
           100:'C', 90:'XC', 50:'L', 40:'XL',
           10: 'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    s = ''
    for key, value in dic.items():
        if num >= key:
            s += (num // key) * value
            num = num % key
        if num == 0:
            return s
    return s

if __name__ == '__main__':
    i = 1946
    print(intToRoman(i))