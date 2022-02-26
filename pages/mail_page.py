from .base_page import BasePage
from .locators import LoginPageLocators


class MailPage(BasePage):
    def add_product_to_basket(self):
        """ Добавление товара в корзину """
        btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn.click()

    def should_not_be_success_message(self):
        """ Проверка ЧТО ЭЛЕМЕНТ НЕ ПОЯВЛЯЕТСЯ на странице в течение заданного времени """
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "SUCCESS MESSAGE IS PRESENTED, BUT SHOULD NOT BE"
