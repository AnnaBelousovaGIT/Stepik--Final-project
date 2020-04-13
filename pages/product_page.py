from .base_page import BasePage
from .locators import ProductPageLocators

class PageObject (BasePage):
    def should_be_button_add_to_basket(self):
        # проверяем, что текущий url адрес содержит кнопку Basket
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        assert basket_button, "Basket button is not found"


    def should_be_correct_name(self):
        #  Название товара в сообщении должно совпадать с добавленным товаром.
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        basket_name = self.browser.find_element(*ProductPageLocators.BASKET_NAME).text
        assert product_name == basket_name, \
            f"The book name is not correct: '{product_name}' instead of '{basket_name}"
        print(f"Product '{product_name}' in your basket")  # сообщение, что товар добавлен в карзину

    def should_be_correct_price(self):
        # Стоимость корзины совпадает с ценой товара.
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == basket_price, \
            f"The price is not correct: '{product_price}' instead of '{basket_price}'"
        print(f"Basket price = {basket_price}")  # сообщение со стоимостью корзины

