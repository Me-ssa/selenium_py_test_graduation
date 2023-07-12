from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def click_to_btn_on_basket(self):
        bnt = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        bnt.click()

    def should_be_product_url(self):
        link = ProductPageLocators.LINK_PRODUCT_PAGE
        assert "?promo=newYear" in link, f"expected '{'?promo=newYear'}' to be substring of '{link}'"

    def should_be_product_btn_on_basket(self):
        assert ProductPageLocators.BTN_ADD_TO_BASKET, "Btn on basket is not presented"

    def should_be_add_product_on_basket(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_HAS_BEEN_ADDED), (
            "Message about adding is not presented")
        # Затем получаем текст элементов для проверки
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_HAS_BEEN_ADDED).text
        # Проверяем, что название товара присутствует в сообщении о добавлении
        # Это можно было бы сделать с помощью split() и сравнения строк,
        # Но не вижу необходимости усложнять код
        assert product_name in message, "No product name in the message"


    def should_be_price(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRICE), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT), (
            "Product price is not presented")
        # Затем получаем текст элементов для проверки
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        # Проверяем, что цена товара присутствует в сообщении со стоимостью корзины
        assert product_price in message_basket_total, "No product price in the message"