from selenium.webdriver.common.by import By


class MainPageLocators():
     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
     LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
     REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
     BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
     PRODUCT_NAME =(By.TAG_NAME, ".product_main h1")
     BASKET_NAME = (By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-success.fade.in .alertinner  strong")
     PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
     BASKET_PRICE = (By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner  strong")
     SUCCESS_MESSAGE=(By.CSS_SELECTOR, "div.alertinner ")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    BUTTON_BASKET_FROM_HEADER_PAGE =(By.CSS_SELECTOR, ".basket-mini > span > a") #кнопка просмотр корзины
    MESSAGE_OF_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner") # сообщение "ваша корзина пуста"


