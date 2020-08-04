#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Create time : 2020/7/22 16:49
@Author      : zhang li
@Version     : 1.0
'''

# Here put the import lib

def missingNumber(nums):
    goal = 0
    if nums[0] != 0:
        return 0
    elif len(nums) != nums[-1]:
        return len(nums)
    else:
        for index, i in enumerate(nums):
            if index != i:
                return index


def missingNumber2(nums):
    # NB
    i, j = 0, len(nums)-1
    while i <= j:
        m = (i+j) // 2
        if nums[m] == m: i = m+1
        else: j = m - 1
    return i


if __name__ == '__main__':

    l = [0,1,2,3,4,5,6,7,9]

    r = missingNumber2(l)
    print(r)