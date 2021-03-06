from locators.Login import Login
from .BasePage import BasePage


class CMSPages(BasePage):

    def __init__(self, chrome):
        self.chrome = chrome

    def login(self, login, password):
        ''' Логин в CMS'''

        # переходим напрямую на страницу логина
        self.chrome.get('https://s1.demo.opensourcecms.com/wordpress/wp-login.php')

        self.chrome.find_element(*Login.username).send_keys(login)
        self.chrome.find_element(*Login.password).send_keys(password)
        self.chrome.find_element(*Login.confirm).click()

    def input_text(self, locator, text):
        self.chrome.find_element(*locator).send_keys(text)
        return self

    def click(self, locator):
        self.chrome.find_element(*locator).click()
        return self

    def get_text(self, locator):
        return self.chrome.find_element(*locator).text
