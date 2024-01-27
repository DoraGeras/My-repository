from pages.base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS), \
"Basket is not empty" 
    
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
"No text about the content of the basket"
        
        

    