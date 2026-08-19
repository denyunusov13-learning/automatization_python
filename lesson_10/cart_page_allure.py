from selenium.webdriver.common.by import By
import allure


class Cart_Page:

    # Константы - локаторы необходимых элементов
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        """
        Инициализация страницы корзины
        :param driver: экземпляр WebDriver (браузер)
        :return: None
        """
        self.driver = driver

    @allure.step("переход на страницу рассчета стоимости")
    def checkout_click(self):
        """
        Нажимает на кнопку checkout и переходит на страницу
        заполнения данных о покупателе
        :return: None
        """
        checkout_btn = self.driver.find_element(*self.CHECKOUT_BUTTON)
        self.driver.execute_script(
            "arguments[0].scrollIntoView();", checkout_btn)
        checkout_btn.click()
