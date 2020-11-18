# -*- coding: utf-8 -*-
# @Time : 2019/7/10 9:57
# @Author : Administrator 艾强云
# @File : pa1.py
# @Software: PyCharm
import urllib.request

def get_proxy_from_cnproxy():
    for i in range(1, 10):
        target = r"http://www.baidu.com"
        print(target)
        req = urllib.request.urlopen(target)
        print(req.read())
get_proxy_from_cnproxy()