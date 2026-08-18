from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Checkout_Page:

    # Константы - локаторы необходимых элементов
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POST_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_PRICE_VALUE = (By.CSS_SELECTOR, "div[data-test='total-label']")

    def __init__(self, driver):
        """
        Инициализация страницы корзины
        :param driver: экземпляр WebDriver (браузер)
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Заполнение поля {FIRST_NAME_FIELD} значением 'Денис'")
    def fill_first_name_field(self):
        """
        ощичает и заполняет поле 'First name'
        """
        firstname_field = self.wait.until(EC.element_to_be_clickable(
                self.FIRST_NAME_FIELD))
        firstname_field.clear()
        firstname_field.send_keys("Денис")

    @allure.step("Заполнение поля {LAST_NAME_FIELD} значением 'Юнусов'")
    def fill_last_name_field(self):
        """
        ощичает и заполняет поле 'Last name'
        """
        lastname_field = self.driver.find_element(*self.LAST_NAME_FIELD)
        lastname_field.clear()
        lastname_field.send_keys("Юнусов")

    @allure.step("Заполнение поля {POST_CODE_FIELD} значением '633456'")
    def fill_post_code_field(self):
        """
        ощичает и заполняет поле 'Post code'
        """
        post_code_field = self.driver.find_element(*self.POST_CODE_FIELD)
        post_code_field.clear()
        post_code_field.send_keys("633456")

    @allure.step("Нажать на кнопку 'продолжить'")
    def click_continue_btn(self):
        """
        Нажимает на кнопку 'continue'
        """
        continue_btn = self.driver.find_element(*self.CONTINUE_BUTTON)
        continue_btn.click()

    @allure.step("Получить итоговое значение стоимости всех товаров")
    def get_total_price_value(self):
        """
        Нажимает на кнопку 'continue'
        :return: str - текстовое выражение значения общей стоимости
        """
        total_price_value = self.wait.until(EC.visibility_of_element_located(
                self.TOTAL_PRICE_VALUE))
        self.driver.execute_script(
            "arguments[0].scrollIntoView();", total_price_value)
        return total_price_value.text
