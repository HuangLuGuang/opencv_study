# -*- coding: utf-8 -*-
# @createTime    : 2019/6/24 23:32
# @author  : Huanglg
# @fileName: 11_阈值.py
# @email: luguang.huang@mabotech.com
import cv2
import numpy as np

from matplotlib import pyplot as plt

img = cv2.imread("images/harder.png", 0)
# 中值滤波
img = cv2.medianBlur(img, 5)

ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
thresh3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

titles = ["Original Image", "BINARY", "BINARY_INV", "TRUNC", "TOZERO", "TOZERO_INV"]
images = [img, thresh1, thresh2, thresh3]

for i in range(4):
    plt.subplot(2, 2, i+1),plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()







