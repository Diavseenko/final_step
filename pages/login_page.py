from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        base_page = self.browser.current_url
        base_page.find("login")
        # реализуйте проверку на корректный url адрес
        assert base_page.find("login") != -1, "This page has not login form"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert BasePage.is_element_present(self, *LoginPageLocators.LOGIN_FORM), "This page is not contains login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert BasePage.is_element_present(self, *LoginPageLocators.REG_FORM), "This page is not contains registration form"

