#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2


# 匹配图片
def mathc_img(image, target_image, value):
    img_rgb = cv2.imread(image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(target_image, 0)
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if max_val < value:
        return 0, 0

    return max_loc
