from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasePageLocators 
from .login_page import LoginPage

class MainPage(BasePage):
    #заглушка:
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

