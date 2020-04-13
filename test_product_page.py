from pages.product_page import PageObject
import pytest


@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", pytest.param(7, marks=pytest.mark.xfail), "8", "9"])

def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = PageObject(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_name()
    page.should_be_correct_price()


