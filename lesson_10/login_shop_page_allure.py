from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Login_Page:

    # Константы - локаторы необходимых элементов
    USERNAME_FIELD = (By.ID, "user-name")
    PASS_FIELD = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "login-button")

    def __init__(self, driver) -> None:
        """
        Инициализация страницы входа в интернет-магазин
        :param driver: экземпляр WebDriver (браузер)
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("открытие страницы магазина")
    def open(self) -> None:
        """
        Открывает страницу интернет-магазина
        :return: None
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("открытие страницы магазина")
    def login(self) -> None:
        """
        Выполняет вход с тестовыми данными.
        :return: ничего (None)
        """
        with allure.step("Вводим логин 'standard_user'"):
            username_field = self.wait.until(
                EC.element_to_be_clickable(self.USERNAME_FIELD))
            username_field.clear()
            username_field.send_keys("standard_user")
        with allure.step("Вводим пароль 'secret_sauce'"):
            pass_field = self.driver.find_element(*self.PASS_FIELD)
            pass_field.clear()
            pass_field.send_keys("secret_sauce")
        with allure.step("нажимаем кнопку 'submit'"):
            login_button = self.driver.find_element(*self.SUBMIT_BUTTON)
            login_button.click()
