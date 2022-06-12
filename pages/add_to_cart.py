from .base_page import BasePage
from .locators import CartLocators
import time


class AddToCart(BasePage):

    def click(self):
        add_button = self.browser.find_element(*CartLocators.LOGIN_FORM)
        add_button.click()

    def check_add_to_cart(self):
        add_message = self.browser.find_element(*CartLocators.ADD_MESSAGE)
        purchase_name = self.browser.find_element(*CartLocators.PURCHASE_NAME)
        assert add_message.text == purchase_name.text, "Check your purchase"

    def check_sum_in_cart(self):
        cart_sum = self.browser.find_element(*CartLocators.CART_SUM)
        purchase_prise = self.browser.find_element(*CartLocators.PURCHASE_PRICE)
        print(cart_sum.text)
        print(purchase_prise.text)
        assert cart_sum.text.find(purchase_prise.text) != -1, "The cart`s sum have a differ with price"



