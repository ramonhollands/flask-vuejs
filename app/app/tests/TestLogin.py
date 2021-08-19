import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from BaseBrowerTestClass import BaseBrowerTestClass
from Pages.LoginPage import LoginPage

class TestLogin(BaseBrowerTestClass):

    def test_login_as_admin(self):
        login_page = LoginPage(self.browser)
        login_page.login_as_default_admin()
        login_page.assert_logged_in()
