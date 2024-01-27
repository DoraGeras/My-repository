from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException     
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from pages.locators import BasePageLocators
#to do

import time
import math

class BasePage():
    def __init__(self, browser, url, timeout=10):  
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)      

    def open(self):
        self.browser.get(self.url)     #открывает вебстраницу (вместо browser.get(link))
    
    #методы из main_page.py и login_page.py(добавлены в п.4.3.8):
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click() 
        
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

    # Метод для перехватывания исключения. args: how (css, id, xpath и тд), what (строку-селектор). try/except
    def is_element_present(self, how, what):       
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True        

    #ожидаем, что элемент не появится на странице в течении опр.времени
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(expected_conditions.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    #ожидаем,что элемент должен исчезнуть в теч.определенного времени
    def is_disappeared(self, how, what, timeout=4):
        try:
             WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                 until_not(expected_conditions.presence_of_element_located((how, what)))
        except TimeoutException:
             return False
        return True


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(1)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

