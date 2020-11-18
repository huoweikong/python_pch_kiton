# -*- coding: utf-8 -*-
# @Time : 2019/8/8 11:48
# @Author : Administrator 艾强云
# @File : fibonacci.py
# @Software: PyCharm

def fib(n):
    if n < 3:
        # print('1' + ', ', end='')
        return 1
    else:
        # a = fib(n-1) + fib(n-2)
        # print(str(a) + ', ',end="")
        return fib(n-1) + fib(n-2)




if __name__ == "__main__":
    f = fib(20)
    print("斐波那契数列为：{}（20）".format(f))

