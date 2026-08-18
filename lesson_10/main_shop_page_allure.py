from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Main_Shop_Page:

    # Константы - локаторы необходимых элементов
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    ADD_BOLT_T_SHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_FLEECE_JACKET = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    ADD_LABS_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    ADD_T_SHIRT_RED = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    CART = (By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")

    def __init__(self, driver):
        """
        Инициализация главной страницы магазина
        :param driver: экземпляр WebDriver (браузер)
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # словарь локаторов по названиям
        self.products = {
            "backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
            "bike light": (By.ID, "add-to-cart-sauce-labs-bike-light"),
            "bolt t shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            "fleece jacket": (By.ID, "add-to-cart-sauce-labs-fleece-jacket"),
            "labs onesie": (By.ID, "add-to-cart-sauce-labs-onesie"),
            "shirt red": (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)"),
            }

    @allure.step("Добавить товар в корзину по части названия: '{part_name}'")
    def add_thing(self, part_name: str) -> None:
        """
        Ищет товар по частичному совпадению названия и добавляет его в корзину.

        :param part_name: Часть названия товара (регистр не учитывается).
        :raises ValueError: Если товар с указанной подстрокой не найден.
        """
        part_name_lower = part_name.lower()
        for full_name, locator in self.products.items():
            if part_name_lower in full_name:
                button = self.wait.until(EC.element_to_be_clickable(locator))
                button.click()
                return
        raise ValueError(f"Товар с подстрокой '{part_name}' не найден")

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        """
        нажимает кнопку корзины и переходит
        на страницу с выбранными товарами
        """
        cart_btn = self.wait.until(EC.element_to_be_clickable(self.CART))
        self.driver.execute_script("arguments[0].scrollIntoView();", cart_btn)
        cart_btn.click()
