from selenium.webdriver.common.by import By


class MainPageLocators():
     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
     LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
     REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
     BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

     PRODUCT_NAME =(By.TAG_NAME, "h1")
     BASKET_NAME = (By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-success.fade.in .alertinner  strong")

     PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
     BASKET_PRICE = (By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner  strong")

