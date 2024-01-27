import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import time


promo_product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
product_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = promo_product_link
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.item_name_check_in_alert_message()
    page.price_check_in_alert_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = product_link
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_item_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = product_link
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = product_link
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_item_to_basket()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = product_link
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = product_link
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = product_link
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_be_empty_basket()


@pytest.mark.authorized_user_tests
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = product_link
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = "stepik_test"
        login_page.register_new_user(email=email, password=password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = promo_product_link
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = promo_product_link
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()
        page.add_item_to_basket()
        page.solve_quiz_and_get_code()
        page.item_name_check_in_alert_message()
        page.price_check_in_alert_message()
