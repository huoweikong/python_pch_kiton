# -*- coding: utf-8 -*-
# @Time : 2019/11/10 11:21
# @Author : Administrator 艾强云
# @File : qiong24.py
# @Software: PyCharm
import itertools


def twentyfour(cards):
    for nums in itertools.permutations(cards):
        for ops in  itertools.protduct('+-*/', repeats = 3):
            bds1 = '({0}{4}{1}){5}({2}{6}{3})'.format(*nums, *ops)
            bds2 = '(({0}{4}{1}){5}{2}){6}{3}'.format(*nums, *ops)
            bds3 = '{0}{4}({1}{5}({2}{6}{3}))'.format(*nums, *ops)

            for bds in [bds1, bds2, bds3]:
                try:
                    if abs(eval(bds) - 24.0) < 1e-10:
                        return bds
                except ZeroDivisionError:
                    continue
    return 'Not Found!'

cards = [1,2,3,4,5,6,7,8,9]
for card in cards:
    print(twentyfour(card))
