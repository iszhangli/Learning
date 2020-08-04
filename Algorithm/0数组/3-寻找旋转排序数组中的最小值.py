#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Create time : 2020/7/24 15:53
@Author      : zhang li
@Version     : 1.0
'''

# Here put the import lib
'''
输入: [2,2,2,0,1]
输出: 0
'''

def findMin(nums):
    i, j = 0, len(nums)-1
    while i<j:
        m = (i+j) // 2
        if nums[j] < nums[m]:
            i = m + 1
        elif nums[j] > nums[m]:
            j = m
        else:
            j = j-1
    return nums[i]

if __name__ == '__main__':
    l = [2,2,2,0,1]
    print(findMin(l))
