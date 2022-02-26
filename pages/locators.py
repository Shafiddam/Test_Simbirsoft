from selenium.webdriver.common.by import By


class BasePageLocators():
    MAIL_LINK = (By.CSS_SELECTOR, "div.desk-notif-card__login-new-item-title")
    MAIL_ENTER_LINK = (By.CSS_SELECTOR, "div.div.desk-notif-card__mail-title")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, ".desk-notif-card__login-new-item desk-notif-card__login-new-item_mail")
    BUTTON2_ENTER = (By.CSS_SELECTOR, ".button2_theme_mail-white")
    INPUT_REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#passp-field-login")
    BUTTON_INPUT_EMAIL = (By.CSS_SELECTOR, ".Button2_type_submit")
    BUTTON_INPUT2_EMAIL = (By.CSS_SELECTOR, ".Button2_type_submit")
    BUTTON_NOT_NOW = (By.CSS_SELECTOR, ".Button2_view_pseudo")
    INPUT_PASSWORD1 = (By.CSS_SELECTOR, ".Textinput-Control")

class MailPageLocators():
    TITLE = (By.CSS_SELECTOR, "[title='Simbirsoft Тестовое задание']")
    BUTTON_WRITE_MAIL = (By.CSS_SELECTOR, ".mail-ComposeButton-Text")
    FIELD_ADDRESS = (By.CSS_SELECTOR, "div.MultipleAddressesDesktop-Field")
    FIELD_TEXT = (By.CSS_SELECTOR, ".cke_wysiwyg_div")




