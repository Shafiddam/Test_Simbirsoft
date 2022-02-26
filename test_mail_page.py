import time

from .pages.base_page import BasePage
import pytest


def test_mail(browser):
    """
    Предварительно необходимо иметь/завести почтовый ящик в google (или
    yandex, если будут проблемы с автоматизацией). Отправить на этот ящик
    несколько писем с темой «Simbirsoft Тестовое задание» с любым содержимым
    (можно отправить с этого же ящика самому себе).
    В задании необходимо:
    1) Использовать Python/Java, подключить библиотеку Selenium Webdriver;
    2) С помощью Selenium открыть браузер, открыть страницу выше указанной
    почты(google.com/yandex.ru) и авторизоваться;
    3) С помощью Selenium определить сколько во входящих нашлось писем с
    темой «Simbirsoft Тестовое задание»;
    4) С помощью Selenium и интерфейса почты написать/отправить письмо на
    этот же почтовый ящик, в тексте которого указать найденное в шаге 3
    количество писем. Указать тему письма «Simbirsoft Тестовое задание.
    <Фамилия>», где <Фамилия> - это Ваша фамилия;
    5) Оформить эти действия в виде теста.
    При выполнении работы необходимо использовать следующие
    технологии:
    1) Selenium GRID (тесты запускать через GRID обязательно)
    2) Использовать паттерн проектирования автотестов Page Object
    3) Реализовать формирование отчетов о пройденных тестах через Allure
    """
    link = 'http://mail.yandex.ru'
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_mail_page()
    # time.sleep(3)
    page.find_count_mail(a=None, count=None)
    page.write_mail()





# class TestUserAddToBasketFromProductPage():
#     @pytest.fixture(scope="function", autouse=True)
#     def setup(self, browser, email=None, password=None):
#         """"
#         открыть страницу регистрации;
#         зарегистрировать нового пользователя;
#         проверить, что пользователь залогинен.
#         """
#         login_link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
#         page = LoginPage(browser, login_link)
#         page.open()
#         page.register_new_user(email, password)
#         page.should_be_authorized_user()
#
#     def test_user_can_add_product_to_basket(self, browser):
#         """
#         Проверка нажатия на кнопку ADD_TO_BASKET_BUTTON
#         Ожидаемый результат:
#         1) Сообщение о том, что товар добавлен в корзину.
#         Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
#         2) Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
#         """
#         product_link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207'
#         page = ProductPage(browser, product_link)
#         page.open()
#         page.add_product_to_basket()
#         page.should_be_msg_about_adding()
