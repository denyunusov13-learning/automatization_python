import pytest
from selenium import webdriver
from lesson_10.login_shop_page_allure import Login_Page
from lesson_10.cart_page_allure import Cart_Page
from lesson_10.checkout_page_allure import Checkout_Page
from lesson_10.main_shop_page_allure import Main_Shop_Page
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование интернет-магазина")
@allure.description("Тест проверяет корректность работы"
                    " интернет-магазина при нажатии"
                    " на различные кнопки и добавлении 3 товаров"
                    " в корзину, и подсчет итоговой цены")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
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
    with allure.step("Проверка итоговой стоимости товаров"):
        assert "$58.29" in total_price, f"Итоговая сумма {total_price}, не $58.29"
