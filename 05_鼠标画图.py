# -*- coding: utf-8 -*-
# @createTime    : 2019/6/18 11:08
# @author  : Huanglg
# @fileName: 5_鼠标画图.py
# @email: luguang.huang@mabotech.com
import cv2
import numpy as np
events=[i for i in dir(cv2) if "EVENT" in i]

def draw_circle(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 100, (255,0,0),-1)

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
