#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Create time : 2020/7/23 17:31
@Author      : zhang li
@Version     : 1.0
'''

# Here put the import lib

'''
输入： board = ["O X"," XO","X O"]
输出： "X"
输入： board = ["OOX","XXO","OXO"]
输出： "Draw"
输入： board = ["OOX","XXO","OX "]
输出： "Pending"
'''

def tictactoe(board):
    n = len(board)
    flag = False

    for i in range(n):
        # 行
        s = board[i]
        if ' ' in s: flag = True
        if len(set(s)) == 1 and s[0] != ' ':
            return s[0]

        # 列
        l = [board[j][i] for j in range(n)]
        if ' ' in l: flag = True
        if len(set(l)) == 1 and l[0] != ' ':
            return l[0]

    # 对角线
    l = [board[i][i] for i in range(n)]
    if len(set(l)) == 1 and l[0] != ' ':
        return l[0]
    l = [board[i][n-i-1] for i in range(n)]
    if len(set(l)) == 1 and l[0] != ' ':
        return l[0]

    # 结果
    if flag is False:
        return 'Draw'
    else:
        return 'Pending'

if __name__ == '__main__':
    board = ["  XO X  ","  XO OX ","O  O    ","   O  X "," XOO    ","  XO XO ","   O  X ","X  OX   "]
    print(tictactoe(board))
