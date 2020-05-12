from selenium.webdriver.common.by import By

class CMS:

    logo_dashboard = (By.CSS_SELECTOR, '#adminmenu')

    category_name = (By.CSS_SELECTOR, '#tag-name')
    add_category = (By.CSS_SELECTOR, '#submit')
    category_added = (By.CSS_SELECTOR, '.row-title')

    post_name = (By.CSS_SELECTOR, '#post-title-0')
    post_content = (By.CSS_SELECTOR, '#content_ifr')

    categories_list = (By.CSS_SELECTOR, '#categorychecklist li')

    add_post = (By.CSS_SELECTOR, '#publish')
