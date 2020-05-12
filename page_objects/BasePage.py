from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, chrome):
        self.chrome = chrome

    def find_element(self, locator, time = 10):
        return WebDriverWait(self.chrome, time).until(EC.presence_of_element_located(locator), message = f'Элемент не найден {locator}!')

    def find_elements(self, locator, time = 10):
        return WebDriverWait(self.chrome, time).until(EC.presence_of_all_elements_located(locator), message = f'Элементы не найдены {locator}!')

