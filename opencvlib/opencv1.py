# -*- coding: utf-8 -*-
# @Time : 2019/11/4 13:14
# @Author : Administrator 艾强云
# @File : opencv1.py
# @Software: PyCharm

import cv2
lena=cv2.imread("test.jpg")
cv2.namedWindow("lesson")
cv2.imshow("lesson",lena)
cv2.waitKey()