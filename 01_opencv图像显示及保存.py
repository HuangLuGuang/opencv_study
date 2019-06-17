# -*- coding: utf-8 -*-
# @createTime    : 2019/6/17 23:30
# @author  : Huanglg
# @fileName: 01_opencv图像显示及保存.py
# @email: luguang.huang@mabotech.com
import numpy as np
import cv2
# 读取图片
img = cv2.imread("images/harder.png", cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow("image", img)
k = cv2.waitKey(0)
if k == "27":
    cv2.destroyAllWindows()
    print("k=",k)
else:
    cv2.imwrite("images/harder_gray.png", img)
    cv2.destroyAllWindows()
    print("save img")
