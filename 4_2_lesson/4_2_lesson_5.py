import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture(scope="function")
def browser():
    # Инициализация WebDriver для браузера (например, Chrome)
    driver = webdriver.Chrome()

    # Установка ожидания неявного ожидания
    driver.implicitly_wait(5)

    # Передача WebDriver в тест
    yield driver

    # Закрытие браузера после завершения теста
    driver.quit()


class MainPage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def should_be_login_link(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    try:
        page.should_be_login_link()
    except NoSuchElementException:
        pytest.fail("Login link is not present on the page")
