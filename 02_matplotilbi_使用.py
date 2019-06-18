# -*- coding: utf-8 -*-
# @createTime    : 2019/6/17 23:46
# @author  : Huanglg
# @fileName: 02_matplotilbi_使用.py
# @email: luguang.huang@mabotech.com
import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread("images/harder.png", cv2.IMREAD_GRAYSCALE)
plt.imshow(img, cmap="gray", interpolation="bicubic")

plt.xticks([]),plt.yticks([])  #to hide tick values on X and Y axis
plt.show()
