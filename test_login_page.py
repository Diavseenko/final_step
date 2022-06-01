from .pages.login_page import LoginPage
from .pages.main_page import MainPage


def test_existing_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    check_login = LoginPage(browser, browser.current_url)
    check_login.should_be_login_url()

def test_existing_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_form = LoginPage(browser, browser.current_url)
    login_form.should_be_login_form()

def test_existing_reg_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    reg_form = LoginPage(browser, browser.current_url)
    reg_form.should_be_register_form()
