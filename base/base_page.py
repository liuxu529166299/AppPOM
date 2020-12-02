# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @File     :base_page
# @Date     :2020/12/1 12:14
# @Author   :刘旭
-------------------------------------------------
"""
from selenium.webdriver.support.wait import WebDriverWait

from logger.logger import LoggerInfo
from base.start_param import get_driver


log = LoggerInfo().logger()

class BasePage():
    def __init__(self,driver):
        # self.driver =get_driver()
        self.driver =driver
        log.info("启动app。。。。。。")

    # 定位元素
    def find_el(self,loc):
        try:
            self.driver.implicitly_wait(10)
            return self.driver.find_element(*loc)
            # return WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(*loc))
        except Exception as e:
            log.error('元素单位失败。。。。s%',e)
    # 点击
    def find_el_click(self,loc):
        self.find_el(loc).click()

    # 输入
    def find_el_sendkeys(self,loc,text):
        self.find_el(loc).send_keys(text)

    # 清除文本内容
    def clear(self,loc):
        self.find_el(loc).clear()

    # 退出
    def quit(self):
        self.driver.quit()
        log.info("退出app。。。。。。")