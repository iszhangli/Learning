'''
1. 交换相邻的元素
'''
# Create time: 2020/6/5 16:23
# Author: zhang li

def bubble_sort(list, asc=True):
    l = list
    length = len(l)
    for i in range(length-1):
        for j in range(length-1-i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


def select_sort(list, asc=True):
    l = list
    for i in range(len(l)-1):
        min_index = i
        for j in range(i+1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]
    return l

if __name__ == '__main__':
    l = [3, 38, 5, 44, 15, 26, 27, 46, 47, 48, 50]
    l = select_sort(l)
    print(l)