from .base_page import BasePage
from .locators import BasePageLocators
from .locators import ProductPageLocators
from .locators import BasketPageLocators

class ProductPage(BasePage):

    #метод-нажать кнопку "Добавить в корзину"
    def add_to_basket(self):
       add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON) 
       add_to_basket_button.click()
    
    #должна быть кнопка "Добавить в корзину"
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not present"
    
    #должно быть сообщение об успешном добавлении товара в корзину
    def should_be_added_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), "Added-to-basket message is not present"
    
    #название товара в сообщении должно совпадать с тем товаром, который добавили
    def added_to_basket_message_is_correct(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_to_basket_product_name = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_PRODUCT_NAME).text
        assert product_name == added_to_basket_product_name, "Incorrect message"
    
    #должно быть сообщение с общей стоимостью товаров к корзине
    def should_be_basket_total_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MESSAGE), "No basket total message"
    
    #стоимость, указанная в корзине, должна совпадать со стоимостью добавленной книги
    def basket_total_price_is_correct(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE_PRICE).text
        assert product_price == basket_total_price, "Incorrect basket total price"
    
    #ожидаем, что нет сообщения об успешном добавлении в корзину
    def should_not_be_added_to_basket_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), \
        "Success added-to-basket message is presented, but should not be"

    #элемент присутствует на странице и должен исчезнуть
    def should_disappear_added_to_basket_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), \
        "Success added-to-basket message is not disappeared, but should be"
    

    