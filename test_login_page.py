import pytest
from pages.login_page import LoginPage
"""
link could be placed in corresponding class in prod
(LoginPage there as example)
"""


@pytest.mark.login_guest
class TestLoginFromMainPage():
    
    def test_guest_should_see_login_form(self, browser):
        link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_form()
    
    def test_guest_should_see_register_form(self, browser):
        link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_register_form()

    def test_login_page_url_should_contain_login_word(self,browser):
        link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()