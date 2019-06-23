# -*- coding: utf-8 -*-
# @createTime    : 2019/6/23 19:56
# @author  : Huanglg
# @fileName: 08_物体追踪.py
# @email: luguang.huang@mabotech.com
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    ret, frame = cap.read()

    # RGB -> HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 设定蓝色的阈值
    lower_blue = np.array([100,50,50])
    upper_blue = np.array([130,255,255])

    # 根据阈值构建掩模
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # 对原图像和掩模进行位运算
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # 显示图像
    cv2.imshow('frame', frame)
    cv2.imshow('hsv', hsv)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()
