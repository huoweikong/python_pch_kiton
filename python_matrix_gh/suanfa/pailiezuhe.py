# -*- coding: utf-8 -*-
# @Time : 2019/11/10 11:45
# @Author : Administrator 艾强云
# @File : pailiezuhe.py
# @Software: PyCharm

# from itertools import combinations #4个里面不允许出现重复
# print(list(combinations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4)))
import itertools
from itertools import product
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(list(product(l, l)))
l1 = list(product(l, repeat=4))
#print(l1)
print(len(l1))
l2 = []
print(len(l2))
for i in l1:
    l2.append(list(i))
#print(l2)



def twentyfour(cards):
    '''史上最短计算24点代码'''
    for nums in itertools.permutations(cards):  # 四个数
        for ops in itertools.product('+-*/', repeat=3):  # 三个运算符（可重复！）
            # 构造三种中缀表达式 (bsd)
            bds1 = '({0}{4}{1}){5}({2}{6}{3})'.format(*nums, *ops)  # (a+b)*(c-d)
            bds2 = '(({0}{4}{1}){5}{2}){6}{3}'.format(*nums, *ops)  # (a+b)*c-d
            bds3 = '{0}{4}({1}{5}({2}{6}{3}))'.format(*nums, *ops)  # a/(b-(c/d))

            for bds in [bds1, bds2, bds3]:  # 遍历
                try:
                    if abs(eval(bds) - 24.0) < 1e-10:  # eval函数
                        return bds
                except ZeroDivisionError:  # 零除错误！
                    continue

    return 'Not found!'
for card in l2:
    print(twentyfour(card))