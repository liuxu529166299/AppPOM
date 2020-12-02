# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @File     :test_login
# @Date     :2020/12/1 12:30
# @Author   :刘旭
-------------------------------------------------
"""
import pytest
from base.start_param import *
from page.page_login import PageLogin

class TestLogin():
    def setup_method(self):
        self.driver = get_driver()

    def test_login_1(self):
        pl=PageLogin(self.driver)
        pl.login_operation(2596546949,"zxcvbnm123..")
        assert_value =pl.login_succese_assert()
        assert assert_value

    def test_login_2(self):
        pl = PageLogin(self.driver)
        pl.login_operation(2596546949, "3432244")
        assert_value = pl.login_fail_assert()
        assert assert_value

    def teardown_method(self):
        self.driver.quit()

# if __name__ == '__main__':
#     pytest.main(["-s", "./test_case/test_login.py"])