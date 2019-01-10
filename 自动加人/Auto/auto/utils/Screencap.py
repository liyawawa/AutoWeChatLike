#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import Constant


# 截图
def screencap():
    # 截图前，先清空文件夹

    if os.path.exists(Constant.my_file):
        # 删除文件，可使用以下两种方法。
        os.remove(Constant.my_file)
        # os.unlink(my_file)
    else:
        print 'no such file:%s' % Constant.my_file

    os.system('adb shell /system/bin/screencap -p /sdcard/screenshot.png')
    os.system('adb pull /sdcard/screenshot.png /Users/liya/Downloads/screenshot/')

    return
