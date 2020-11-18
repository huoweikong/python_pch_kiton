# -*- coding: utf-8 -*-
# @Time : 2019/10/31 19:03
# @Author : Administrator 艾强云
# @File : pyplot1.py
# @Software: PyCharm
import matplotlib.pyplot as plt

x = range(-100,101)
y=[i**2 for i in x]

plt.plot(x,y)

plt.savefig('./fdfdf.svg')
plt.show()