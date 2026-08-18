import pytest
from selenium import webdriver
from lesson_07.pages.calc_page import Calc_Page
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование калькулятора: {sequence}")
@allure.description("Тест проверяет корректность работы"
                    " калькулятора с различными операциями"
                    " через {field_value} секунд")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc_new(driver):
    calc_page = Calc_Page(driver)
    calc_page.open()
    calc_page.set_timer(5)
    calc_page.click_button(["7", "+", "8", "="])
    calc_page.waiting_fot_the_spinner()
    result = calc_page.get_result()
    with allure.step("Проверка результата после исчезновения спиннера"):
        assert result == "15", f"Ожидалось 15, но получено {result}"
