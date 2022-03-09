import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators, LoginPageLocators, MailPageLocators

email = "Simbirsoft2022"
full_email = "Simbirsoft2022@yandex.ru"
password = "Simbirsoft-2022"


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url

    def go_to_login_page(self):
        """ Кликаем на кнопку логина. """
        link = self.browser.find_element(*BasePageLocators.MAIL_LINK)
        link.click()

    def go_to_login_mail_page(self):
        """ Логинимся в почте: заполняем поля входа. """
        btn = self.browser.find_element(*LoginPageLocators.BUTTON2_ENTER)
        btn.click()
        # вводим имя Simbirsoft2022:
        btn = self.browser.find_element(*LoginPageLocators.INPUT_REGISTRATION_EMAIL)
        btn.send_keys(email)
        # жмем Войти:
        btn = self.browser.find_element(*LoginPageLocators.BUTTON_INPUT_EMAIL)
        btn.click()
        # вводим пароль, нужна пауза, чтобы успеть ввести пароль:
        time.sleep(1)
        btn = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD1)
        btn.send_keys(password)
        # жмем Войти:
        btn = self.browser.find_element(*LoginPageLocators.BUTTON_INPUT_EMAIL)
        btn.click()

    def find_count_mail_and_write_mail(self):
        # нужна пауза чтобы подгрузилась страница и подсчитались письма:
        time.sleep(4)
        # ищем список элементов по теме письма (локатор TITLE):
        a = self.browser.find_elements(*MailPageLocators.TITLE)
        count = len(a)
        btn = self.browser.find_element(*MailPageLocators.BUTTON_WRITE_MAIL)
        btn.click()
        time.sleep(3)
        btn = self.browser.find_element(*MailPageLocators.FIELD_ADDRESS)
        btn.send_keys(full_email)
        btn = self.browser.find_element(*MailPageLocators.FIELD_SUBJECT_TEXT)
        btn.send_keys("Simbirsoft Тестовое задание. Шафиков")
        time.sleep(2)
        btn = self.browser.find_element(*MailPageLocators.FIELD_TEXTBOX_CONTENT_EMAIL)
        btn.send_keys(f"Количество найденных писем: ", count)
        time.sleep(3)
        btn = self.browser.find_element(*MailPageLocators.BUTTON_SEND_MAIL)
        btn.click()
        time.sleep(3)

    def is_element_present(self, how, what):
        """
        Метод, в котором будем перехватывать исключение. В него будем передавать два аргумента:
        как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).
        Чтобы перехватывать исключение, нужна конструкция try/except:
        """
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """
        Абстрактный метод, который проверяет, ___ЧТО ЭЛЕМЕНТ НЕ ПОЯВЛЯЕТСЯ___
        на странице в течение заданного времени:
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """
        Метод, который проверяет, ___ЧТО ЭЛЕМЕНТ ИСЧЕЗАЕТ___
        Следует воспользоваться явным ожиданием вместе с функцией until_not,
        в зависимости от того, какой результат мы ожидаем:
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def open(self):
        """ Открытие браузера """
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        """ Проверка, что пользователь залогинен """
        assert self.is_element_present(*BasePageLocators.USER_ICON), "USER ICON IS NOT PRESENTED," \
                                                                     " PROBABLY UNAUTHORISED USER"

    def should_be_login_link(self):
        """ Проверка, что подстрока "login" есть в текущем url браузера """
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "LOGIN LINK IS NOT PRESENTED"
