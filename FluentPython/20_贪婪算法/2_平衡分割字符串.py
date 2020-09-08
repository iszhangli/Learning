'''
在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。

给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。

返回可以通过分割得到的平衡字符串的最大数量。

s = "RLRRLLRLRL"
输出：4

'''

def balancedStringSplit(s):
    cnt = 0
    balance = 0
    for i in s:
        if i == 'R':
            balance -= 1
        else:
            balance += 1
        if balance == 0:
            cnt += 1
    
if __name__ == "__main__":
    s = "RLRRLLRLRL"
    balancedStringSplit(s)