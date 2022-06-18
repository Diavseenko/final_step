from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def click_to_add_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_MESSAGE), \
            "Success message is presented, but should not be"

    def check_add_to_cart(self):
        add_message = self.browser.find_element(*ProductPageLocators.ADD_MESSAGE_NAME)
        purchase_name = self.browser.find_element(*ProductPageLocators.PURCHASE_NAME)
        assert add_message.text == purchase_name.text, "Check your purchase"

    def check_sum_in_cart(self):
        cart_sum = self.browser.find_element(*ProductPageLocators.CART_SUM)
        purchase_prise = self.browser.find_element(*ProductPageLocators.PURCHASE_PRICE)
        assert cart_sum.text.find(purchase_prise.text) != -1, "The cart`s sum have a differ with price"

    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_MESSAGE), "No message"

    def no_goods_in_cart(self):
        assert self.is_not_element_present(*ProductPageLocators.CART_ITEMS), "No goods in cart"

    def has_a_empty_cart_message(self):
        assert self.is_element_present(*ProductPageLocators.EMPTY_CART), "The message is present"










