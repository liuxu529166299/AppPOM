# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @File     :page_login
# @Date     :2020/12/1 13:15
# @Author   :刘旭
-------------------------------------------------
"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage,log
from base.start_param import get_driver
from time import sleep

# 元素定位与变量
into_el =(By.ID,'com.tencent.mobileqq:id/btn_login')
user_el =(By.CLASS_NAME,'android.widget.EditText')
pwd_el = (By.ID,'com.tencent.mobileqq:id/password')
appPackage="com.tencent.mobileqq"
appActivity='com.tencent.mobileqq.activity.LoginActivity'
login_bu=(By.ID,'com.tencent.mobileqq:id/login')
assert_succese = (By.ID,"com.tencent.mobileqq:id/j_k")
assert_fail = (By.ID,'com.tencent.mobileqq:id/egz')

class PageLogin(BasePage):
    def into_login(self):
        self.find_el_click(into_el)

    # 输入帐号
    def send_user(self,text):
        self.find_el_sendkeys(user_el,text)

    # 输入密码
    def send_pwd(self,text):
        self.find_el_sendkeys(pwd_el,text)

    # 点击登录按钮
    def click_login(self):
        self.find_el_click(login_bu)

    # 登录流程
    def login_operation(self,user,pwd):
        log.info('输入帐号密码登录。。。。。。')
        self.send_user(user)
        self.send_pwd(pwd)
        self.click_login()

    def login_succese_assert(self):
        if self.find_el(assert_succese):
            log.info('登录断言成功。。。。。。')
            return True
        else:
            return False

    def login_fail_assert(self):
        if self.find_el(assert_fail):
            log.info('登录断言成功。。。。。。')
            return True
        else:
            return False

# pl =PageLogin(get_driver())
# pl.send_user(user_el,666666666)
# pl.quit()
