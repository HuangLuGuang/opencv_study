# -*- coding: utf-8 -*-
# @createTime    : 2019/6/20 19:22
# @author  : Huanglg
# @fileName: 07_获取并修改像素.py
# @email: luguang.huang@mabotech.com
import cv2
import numpy as np

img = cv2.imread("images/1.png")

px = img[100,100]
blue = img[100,100,0]
print(type(img))
print(img)
print(img.shape)
print(px)
print(blue)
