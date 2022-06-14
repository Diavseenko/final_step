from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class CartLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADD_MESSAGE_NAME = (By.CSS_SELECTOR, "div .alertinner strong")
    ADD_MESSAGE = (By.CSS_SELECTOR, "div .alertinner")
    PURCHASE_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    CART_SUM = (By.CSS_SELECTOR, ".hidden-xs")
    PURCHASE_NAME = (By.CSS_SELECTOR, ".product_main h1")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
