#!/usr/bin/python
# -*- coding: UTF-8 -*-

from PIL import Image
import pytesseract

import Screencap
import time
import Constant
import os
import MatchPicture


#
#
# os.system('adb shell input tap 100 100')

def doSomething():
    Screencap.screencap()

    if os.path.exists(Constant.my_file):
        print ''
    else:
        print 'no such file:%s' % Constant.my_file


def send():
    image = Constant.my_file
    target_image = Constant.my_file_sendAdd
    value = 0.9

    max_loc = MatchPicture.mathc_img(image, target_image, value)

    if max_loc != (0, 0):
        os.system("adb shell input tap %s %s" % max_loc)
    else:
        print "not found"


def addFriends():
    image = Constant.my_file
    target_image = Constant.my_file_add
    value = 0.9

    max_loc = MatchPicture.mathc_img(image, target_image, value)

    if max_loc != (0, 0):
        os.system("adb shell input tap %s %s" % max_loc)
    else:
        print "not found"


if __name__ == '__main__':

    i = 0

    start = time.clock()

    while True:

        # doSomething()

        # 添加好友
        addFriends()

        # 发送好友
        # send()

        # text=pytesseract.image_to_string(Constant.my_file,lang="chi_sim")
        #
        # print text.replace(" ","")

        # image = Constant.my_file
        # target_image = Constant.my_file_login
        # value = 0.9
        #
        # max_loc = MatchPicture.mathc_img(image, target_image, value)
        #
        # print max_loc
        #
        # os.system("adb shell input tap %s %s" % max_loc)

        i = i + 1

        if i > 0:
            break

    end = time.clock()
    print end - start
