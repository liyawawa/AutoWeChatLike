#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Screencap

import Constant
import wda

driver = wda.Client('http://192.168.100.25:8100')

s = driver.session()

def moveup():
    print 1




def movedown():
    print 2



def moveleft():
    print 3



def moveright():
    print 4



if __name__ == '__main__':
    s.screenshot().save(Constant.my_file)

    s.tap(175,1210)
    # s.tap(140,175)



