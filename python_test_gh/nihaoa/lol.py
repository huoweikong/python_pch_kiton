# -*- coding: utf-8 -*-
# @Time : 2019/6/28 20:56
# @Author : Administrator 艾强云
# @File : lol.py
# @Software: PyCharm https://tieba.baidu.com/f?ie=utf-8&kw=LOL&fr=search
#import beautifulsoap

def load_page(url):
    #发送url请求，返回url清切的静态HTML页面
    usr_agent =
def tieba_spider(url, begin_page, end_page):
    #贴吧小爬虫
    for i in range(begin_page, end_page + 1):
        pn = 50 * (i - 1)
        #组成一个完整的url
        my_url = url + str(pn)
        print("sjgd", my_url)

if __name__ == "__main__":
    print("hello world")
    url = input("请输入网址")
    print(url)
    begin_page = input("请输入起始页码")
    end_page = input("请输入结束页码")

    print(begin_page)
    print((end_page))
