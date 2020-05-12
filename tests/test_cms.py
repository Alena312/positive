from locators.Cms import Cms
from locators.Main import Main
from locators.Login import Login
from page_objects.CMSPages import CMSPages


def test_login_error(chrome):
    ''' Тест, проверяющий ввод невалидных данных при логине в систему
        Ожидаемый результат - ошибка'''

    cms = CMSPages(chrome)
    cms.login('invalid', 'invalid')

    # ждем появление ошибки
    assert cms.find_element(Login.error), 'Ошибка о невалидном логине не отображается!'


def test_login_success(chrome):
    ''' Тест, проверяющий ввод валидных данных при логине в систему
        Ожидаемый результат - успешный логин'''

    cms = CMSPages(chrome)
    cms.login('opensourcecms', 'opensourcecms')

    # ждем перехода в админку и проверяем наличие там элемента
    assert cms.find_element(Cms.logo_dashboard), 'Авторизация не прошла!'


def test_add_category(chrome):
    ''' Тест, проверяющий создание новой категории
        Ожидаемый результат - категория создана'''

    cms = CMSPages(chrome)
    cms.login('opensourcecms', 'opensourcecms')
    # переходим в раздел с категориями
    chrome.get('https://s1.demo.opensourcecms.com/wordpress/wp-admin/edit-tags.php?taxonomy=category')

    # присваиваем новой категории заданное имя
    name = '36484'
    cms.input_text(Cms.category_name, name)

    # подтверждаем сохранение
    cms.click(Cms.add_category)

    # убеждаемся, что новая категория отображена в списке
    cats = cms.find_elements(Cms.categories_added)
    all_cats = []
    for cat in cats:
        all_cats.append(cat.text)

    assert name in all_cats, 'Категория не создана или создана некорректно!'


def test_add_post(chrome):
    ''' Тест, проверяющий добавление нового поста с указанной категорией
        Ожидаемый результат - пост добавлен'''

    cms = CMSPages(chrome)
    cms.login('opensourcecms', 'opensourcecms')
    chrome.get('https://s1.demo.opensourcecms.com/wordpress/wp-admin/post-new.php')

    title = 'Test Post'
    body = 'This Is Test Post'
    category_name = '36484'

    # задаем название поста
    cms.input_text(Cms.post_name, title)

    # вводим текст поста
    cms.click(Cms.post_content)
    cms.input_text(Cms.post_content_active, body)

    cms.click(Cms.doc_tab)
    cms.click(Cms.categories_block)
    # получаем список всех существующих категорий
    categories = cms.find_elements(Cms.categories_list)

    # проходимся по всем категориям, находим категорию с нужным названием и выбираем ее
    for category in categories:
        if category.text == category_name:
            category.find_element(*Cms.category_checkbox).click()

    # публикуем пост
    cms.click(Cms.add_post)
    cms.click(Cms.confirm_add_post)

    # убеждаемся, что пост создан
    cms.find_element(Cms.publish_check)

    # переходим на главную
    chrome.get('https://s1.demo.opensourcecms.com/wordpress/')
    categories = cms.find_elements(Main.categories)

    # фильтруем посты по категории 36484
    for category in categories:
        if category.text == category_name:
            category.click()

    # убеждаемся, что на странице присутствует пост с заголовком Test Post
    posts = cms.find_elements(Main.posts)
    posts_name = []
    for post in posts:
        posts_name.append(post.text)

    assert title in posts_name, 'Новый пост отсутствует на главной странице!'
