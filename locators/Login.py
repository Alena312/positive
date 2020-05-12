from selenium.webdriver.common.by import By

class Login:

    login_form = (By.CSS_SELECTOR, '#loginform')
    username = (By.CSS_SELECTOR, '#user_login')
    password = (By.CSS_SELECTOR, '#user_pass')
    confirm = (By.CSS_SELECTOR, '#wp-submit')

    error = (By.CSS_SELECTOR, '#login_error')
