from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PURCHASE_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PURCHASE_NAME = (By.CSS_SELECTOR, ".product_main h1")
    CART_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_CART = (By.CSS_SELECTOR, "#content_inner :nth-child(1)")
    CART_SUM = (By.CSS_SELECTOR, ".hidden-xs")
    ADD_MESSAGE_NAME = (By.CSS_SELECTOR, "div .alertinner strong")
    ADD_MESSAGE = (By.CSS_SELECTOR, "div .alertinner")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART = (By.CSS_SELECTOR, ".btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

