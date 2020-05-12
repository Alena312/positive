from locators import Cms
from page_objects import LoginPage


def test_login_error(chrome):
    ''' Тест, проверяющий ввод невалидных данных при логине в систему
        Ожидаемый результат - ошибка'''

    cms = LoginPage(chrome)
    cms.login('invalid', 'invalid')

    # ждем появление ошибки
    assert cms.find_element(*LoginPage.error), 'Ошибка о невалидном логине не отображается!'


def test_login_success(chrome):
    ''' Тест, проверяющий ввод валидных данных при логине в систему
        Ожидаемый результат - успешный логин'''

    cms = LoginPage(chrome)
    cms.login('opensourcecms', 'opensourcecms')

    # ждем перехода в админку и проверяем наличие там элемента
    assert cms.find_element(*Cms.logo_dashboard), 'Авторизация не прошла!'


def test_add_category(chrome):
    ''' Тест, проверяющий создание новой категории
        Ожидаемый результат - категория создана'''

    cms = LoginPage(chrome)
    cms.login('opensourcecms', 'opensourcecms')
    # переходим в раздел с категориями
    cms.go_url('https://s1.demo.opensourcecms.com/wordpress/wp-admin/edit-tags.php?taxonomy=category')

    # присваиваем новой категории заданное имя
    name = '36484'
    cms.find_element(*Cms.category_name).send_keys(name)
    # подтверждаем сохранение
    cms.find_element(*Cms.add_category).click()

    # убеждаемся, что новая категория отображена в списке
    new_category = cms.find_element(*Cms.category_added)
    assert new_category.text == name, 'Категория не создана или создана некорректно!'


def test_add_post(chrome):
    ''' Тест, проверяющий добавление нового поста с указанной категорией
        Ожидаемый результат - пост добавлен'''

    cms = LoginPage(chrome)
    cms.login('opensourcecms', 'opensourcecms')
    cms.go_url('https://s1.demo.opensourcecms.com/wordpress/wp-admin/post-new.php')

    title = 'Test Post'
    body = 'This Is Test Post'

    # задаем название поста
    chrome.find_element(*Cms.post_name).send_keys(title)
    # вводим текст поста
    chrome.find_element(*Cms.post_content).send_keys(body)
    # получаем список всех существующих категорий
    categories = chrome.find_elements(*Cms.categories_list)

    # проходимся по всем категориям, находим категорию с нужным названием и выбираем ее
    for category in categories:
        print(category.text)
        if category.text == '36484':
            category.click()

    # публикуем пост
    chrome.find_element_by_css_selector(*Cms.add_post).click()

    # убеждаемся, что пост создан
    # переходим на главную
    # фильтруем посты по категории 36484
    # убеждаемся, что на странице присутствует пост с заголовком Test Post
