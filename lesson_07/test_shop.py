import pytest
from selenium import webdriver
from lesson_07.pages.login_shop_page import Login_Page
from lesson_07.pages.cart_page import Cart_Page
from lesson_07.pages.checkout_page import Checkout_Page
from lesson_07.pages.main_shop_page import Main_Shop_Page


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    login_page = Login_Page(driver)
    cart_page = Cart_Page(driver)
    checkout_page = Checkout_Page(driver)
    main_shop_page = Main_Shop_Page(driver)

    login_page.open()
    login_page.login()

    main_shop_page.add_thing("backpack")
    main_shop_page.add_thing("bolt")
    main_shop_page.add_thing("onesie")

    main_shop_page.go_to_cart()

    cart_page.checkout_click()
    checkout_page.fill_first_name_field()
    checkout_page.fill_last_name_field()
    checkout_page.fill_post_code_field()
    checkout_page.click_continue_btn()

    total_price = checkout_page.get_total_price_value()
    assert "$58.29" in total_price, f"Итоговая сумма {total_price}, не $58.29"
