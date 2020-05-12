from selenium.webdriver.common.by import By

class Cms:

    logo_dashboard      = (By.CSS_SELECTOR, '#adminmenu')

    category_name       = (By.CSS_SELECTOR, '#tag-name')
    add_category        = (By.CSS_SELECTOR, '#submit')
    categories_added      = (By.CSS_SELECTOR, '.row-title')

    post_name           = (By.CSS_SELECTOR, '#post-title-0')
    post_content        = (By.CSS_SELECTOR, '.block-editor-block-list__layout .editor-default-block-appender__content')
    post_content_active = (By.CSS_SELECTOR, '.block-editor-rich-text__editable')

    doc_tab             = (By.CSS_SELECTOR, '.edit-post-sidebar__panel-tab')
    categories_block    = (By.XPATH, '//button[contains(text(), "Categories")]')
    categories_list     = (By.CSS_SELECTOR, '.editor-post-taxonomies__hierarchical-terms-choice')
    category_checkbox   = (By.CSS_SELECTOR, '.editor-post-taxonomies__hierarchical-terms-input')

    add_post            = (By.CSS_SELECTOR, '.editor-post-publish-panel__toggle')
    confirm_add_post    = (By.CSS_SELECTOR, '.editor-post-publish-button')
    publish_check       = (By.CSS_SELECTOR, '.editor-post-publish-panel__header-published')
