# -*- coding: utf-8 -*-
# @createTime    : 2019/6/23 20:51
# @author  : Huanglg
# @fileName: 09_扩展缩放.py
# @email: luguang.huang@mabotech.com
import cv2
import numpy as np

img = cv2.imread("images/harder.png")

res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
#
# height, width = img.shape[:2]
# res = cv2.resize(img, (2*width, 2*height), interpolation=cv2.INTER_CUBIC)

while(1):
    cv2.imshow("res", res)
    cv2.imshow("img", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
