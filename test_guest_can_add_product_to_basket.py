from .pages.add_to_cart import AddToCart
import time


def test_add_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = AddToCart(browser, link)
    page.open()
    page.click()
    page.solve_quiz_and_get_code()
    page.check_add_to_cart()
    page.check_sum_in_cart()




