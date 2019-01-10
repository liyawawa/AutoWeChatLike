#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wda
import time
import random

wda.DEBUG = False  # default False
wda.HTTP_TIMEOUT = 60.0  # default 60.0 seconds

driver = wda.Client('http://192.168.100.25:8100')

wechat_session = driver.session()

x, y = wechat_session.window_size()
scale = wechat_session.scale

xys = []


# time.sleep(random.uniform(1, 1.1))
#
# wechat_session(name=u'泗洲禅寺观光团', type='StaticText').tap()
#
# time.sleep(random.uniform(1, 1.1))
#
# wechat_session(name=u'更多', type='Button').tap()
#
# wechat_session(name=u'查看更多群成员', type='Button').tap()
#

def morebutton():
    try:
        l = wechat_session(className='Button', name=u'添加成员').get().visible
        if l:
            return True
        else:
            return False
    except wda.WDAElementNotFoundError:
        return False


def slide(height):
    print height

    wechat_session.swipe(int(x * scale * 0.5), int(y * scale * 0.5), int(x * scale * 0.2),
                         int(y * scale * 0.5 - height), 0.5)


def addpeople():
    is_add = wechat_session(name=u'添加到通讯录', type='Button').exists

    if is_add:
        wechat_session(name=u'添加到通讯录', type='Button').tap()

        time.sleep(random.uniform(0.4, 0.6))

        is_send = wechat_session(name=u'请求失败', type='StaticText').exists

        if is_send:
            wechat_session(name=u'确定', type='Button').tap()
            time.sleep(random.uniform(0.4, 0.8))
            wechat_session(name=u'返回', type='Button').tap()
        else:
            if wechat_session(name=u'发送', type='Button').exists:
                wechat_session(name=u'发送', type='Button').tap()
            time.sleep(random.uniform(0.6, 0.8))
            wechat_session(name=u'返回', type='Button').tap()
    else:
        wechat_session(name=u'返回', type='Button').tap()


if __name__ == '__main__':

    elements = wechat_session(className='Table').child(className='Cell').child(className='Button').find_elements()

    print elements.__len__()

    # 设定一行个数
    index = 2

    row_num = 10

    while True:
        print '当前行数', index

        pangu_w = elements[index * row_num - 1].bounds.width
        pangu_h = elements[index * row_num - 1].bounds.height
        pangu_x = elements[index * row_num - 1].bounds.x
        pangu_y = elements[index * row_num - 1].bounds.y

        w_j = elements[index * row_num - 2].bounds.x - elements[index * row_num - 3].bounds.x

        for ei in range(row_num):

            ex = (index - 1) * row_num + ei

            if elements[ex].visible:
                t_x = pangu_x + w_j * ei
                t_y = pangu_y

                print t_x + pangu_w / 2, t_y + pangu_h / 2

                wechat_session.tap(t_x + pangu_w / 2, t_y + pangu_h / 2)

                time.sleep(random.uniform(0.5, 0.8))

                addpeople()

        index = index + 1

        if morebutton() is False:
            slide(pangu_y)
