from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REG_EMAIL_LINK = (By.NAME, "#registration-email")
    REG_PASS_LINK = (By. NAME, "registration-password1")
    REG_CONF_PASS_LINK = (By.NAME, "registration-password2")
    LOGIN = (By.NAME, "login-username")
    LOGIN_PASSWORD = (By.NAME, "login-password")