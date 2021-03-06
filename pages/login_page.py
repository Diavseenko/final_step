from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        confirm_password_field.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()

    def should_be_login_url(self):  # реализуйте проверку на корректный url адрес
        base_page = self.browser.current_url
        base_page.find("login")
        assert base_page.find("login") != -1, "This page has not login form"

    def should_be_login_form(self):  # реализуйте проверку, что есть форма логина
        assert BasePage.is_element_present(self, *LoginPageLocators.LOGIN_FORM), "This page is not contains login form"

    def should_be_register_form(self):  # реализуйте проверку, что есть форма регистрации на странице
        assert BasePage.is_element_present(self, *LoginPageLocators.REG_FORM), "This page is not contains " \
                                                                               "registration form"
