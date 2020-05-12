import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.yield_fixture
def chrome():
    '''
    Фикстура для настройки вебрайвера Chrome с заданными аргументами
    '''
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--headless")
    chrome = webdriver.Chrome(options=chrome_options)
    yield chrome
    chrome.quit()