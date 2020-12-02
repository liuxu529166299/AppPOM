# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @File     :start_param
# @Date     :2020/12/1 12:17
# @Author   :刘旭
-------------------------------------------------
"""
from appium import webdriver

# 调试app
# appPackage= 'com.android.settings', appActivity='.Settings'

# 设置默认启动app界面参数
default_package = 'com.tencent.mobileqq'
default_activity = 'com.tencent.mobileqq.activity.LoginActivity'


def get_driver(deviceName='testDevice', appPackage=default_package, appActivity=default_activity):
    desired_caps = dict()
    desired_caps['automationName'] = 'uiautomator2'
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1.2'
    desired_caps['deviceName'] = deviceName
    desired_caps['appPackage'] = appPackage
    desired_caps['appActivity'] = appActivity
    desired_caps['unicodeKeyboard'] = 'True'
    desired_caps['resetKeyboard'] = 'True'
    desired_caps['noReset'] = 'True'
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    return driver
