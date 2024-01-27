from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import time
import math


class ProductPage:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    CART_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")

    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self):
        add_to_cart_button = self.driver.find_element(*self.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def get_success_message(self):
        success_message = self.driver.find_element(*self.SUCCESS_MESSAGE)
        return success_message.text.strip()

    def get_product_price(self):
        product_price = self.driver.find_element(*self.PRODUCT_PRICE)
        return product_price.text.strip()

    def get_cart_price(self):
        cart_price = self.driver.find_element(*self.CART_PRICE)
        return cart_price.text.strip()

    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):

    driver = webdriver.Chrome()

    product_page = ProductPage(driver)


    product_page.add_product_to_cart()


    product_page.solve_quiz_and_get_code()
    time.sleep(30)


    success_message = product_page.get_success_message()
    assert "has been added to your basket" in success_message, "Неверное сообщение об успешном добавлении товара в корзину"


    product_price = product_page.get_product_price()
    cart_price = product_page.get_cart_price()
    assert product_price == cart_price, "Неверная цена товара в корзине"


        # Закрываем браузер
    driver.quit()
