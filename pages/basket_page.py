from .base_page import BasePage
from .locators import ProductPageLocators, BasketPageLocators


class BasketPage(BasePage):


    def should_be_empty_basket(self):
        empty_basket= self.browser.find_element(*BasketPageLocators.MESSAGE_OF_EMPTY_BASKET)
        assert  "Your basket is empty" in empty_basket.text , \
            "Basket is not empty, but should be"



    def should_not_product_in_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Product is presented in basket, but should not be"
