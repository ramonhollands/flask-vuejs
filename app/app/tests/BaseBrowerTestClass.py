import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class BaseBrowerTestClass():
    def setup_class(self):
        pass
    def teardown_class(self):
        pass

    def setup_method(self):
        options = webdriver.ChromeOptions()
        options.headless = True

        self.browser = webdriver.Remote(
            command_executor='http://chrome:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME,
            options=options)

        self.browser.get('http://flask_vuejs_app:8008')
        assert 'Flask app' in self.browser.title

    def teardown_method(self):
        self.browser.quit

    def download_file(self):
        # https://www.browserstack.com/guide/download-file-using-selenium-python
        pass

    def click(self, text):
        link = self.browser.find_element_by_link_text(text)
        link.click()
        return self

    def see(self, needle, tag='body'):
        haystack = self.browser.find_element_by_tag_name(tag).text
        assert needle in haystack
        return self

    def save_screenshot(self):
        self.browser.save_screenshot('screenshot.png')