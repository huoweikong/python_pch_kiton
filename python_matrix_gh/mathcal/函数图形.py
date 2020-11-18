# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# !coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.size'] = 14

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
# 这些是作为单个整数编码的子绘图网格参数。例如，“111”表示“1×1网格，第一子图”，
# “234”表示“2×3网格，第四子图”。
plt.plot([-10, 10], [0, 0], 'gray', ':')
plt.plot([0, 0], [-10, 10], 'gray', ':')

x1 = np.arange(-10, 0, 0.1)
y1 = 1 / x1
plt.plot(x1, y1)

x2 = np.arange(0.1, 10, 0.1)
y2 = 1 / x2
plt.plot(x2, y2)

x3 = np.arange(-10, 10, 0.1)
y3 = [i ** 2 for i in x3]
plt.plot(x3, y3)

x4 = np.arange(-10, 10, 0.1)
y4 = [i ** 3 for i in x3]
plt.plot(x3, y4)

x5 = np.arange(-10, 10, 0.1)
y5 = [i ** 0.5 for i in x3]
plt.plot(x3, y5)

y6 = [i for i in x3]
plt.plot(x3, y6)

plt.xlabel('x')
plt.ylabel('y')
plt.xticks(range(-10, 11, 1))
plt.yticks(range(-10, 11, 1))
ax.set_yticklabels(range(-10, 11, 1))
plt.axis([-10, 10, -10, 10])
plt.title(u'$y=\\frac{1}{x}$')
plt.grid(True)

plt.savefig(u"反比例函数.pdf")
plt.show()