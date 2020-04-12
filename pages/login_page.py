from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert 'login' in self.browser.current_url, "Login link is not found"

    def should_be_login_form(self):
        # проверяем, что есть форма логина
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login Form is not found"

    def should_be_register_form(self):
        # проверяем, что есть форма регистрации на странице
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Register Form is not found"