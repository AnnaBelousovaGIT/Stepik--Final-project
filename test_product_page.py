from pages.product_page import PageObject
from pages.basket_page import BasketPage
import pytest

"""
@pytest.mark.parametrize('promo_offer',
                         ["0", "1", "3", "4", "5", "6", pytest.param(7, marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = PageObject(browser,link)  
    page.open()  
    page.should_be_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_name()
    page.should_be_correct_price()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.go_to_login_page() """


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

"""
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = PageObject(browser, link)
    page.open()
    page.should_be_button_add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = PageObject(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = PageObject(browser, link)
    page.open()
    page.should_be_button_add_to_basket()
    page.should_dissapear_of_success_message()"""


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_header_page()
    page.should_be_empty_basket()
    page.should_not_product_in_basket()



