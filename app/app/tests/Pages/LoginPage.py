from selenium.webdriver.common.keys import Keys

class LoginPage():
    def __init__(self, browser):
        self.browser = browser

    def assert_on_page(self):
        assert 'user/sign-in' in self.browser.current_url

    def login_as_default_admin(self):
        self.login_as('admin@flask.app')

    def login_as(self, username, password='secret'):
        self.assert_on_page()

        inputElement = self.browser.find_element_by_id("email")
        inputElement.send_keys(username)

        inputElement = self.browser.find_element_by_id("password")
        inputElement.send_keys(password)

        inputElement.send_keys(Keys.ENTER)

    def assert_logged_in(self):
        text = self.browser.find_element_by_tag_name('body').text
        assert 'You have signed in successfully' in text

