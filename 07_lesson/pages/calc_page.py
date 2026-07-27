from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calc_Page:

    WAIT_TIMER_FIELD = (By.ID, "delay")
    BUTTON_LOCATORS = {
        "1": (By.XPATH, "//span[text()='1']"),
        "2": (By.XPATH, "//span[text()='2']"),
        "3": (By.XPATH, "//span[text()='3']"),
        "4": (By.XPATH, "//span[text()='4']"),
        "5": (By.XPATH, "//span[text()='5']"),
        "6": (By.XPATH, "//span[text()='6']"),
        "7": (By.XPATH, "//span[text()='7']"),
        "8": (By.XPATH, "//span[text()='8']"),
        "9": (By.XPATH, "//span[text()='9']"),
        "0": (By.XPATH, "//span[text()='0']"),
        "c": (By.XPATH, "//span[text()='C']"),
        ".": (By.XPATH, "//span[text()='.']"),
        "+": (By.XPATH, "//span[text()='+']"),
        "-": (By.XPATH, "//span[text()='-']"),
        "/": (By.XPATH, "//span[text()='÷']"),
        "x": (By.XPATH, "//span[text()='x']"),
        "=": (By.XPATH, "//span[text()='=']"),
    }
    RESULT_FIELD = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_timer(self, field_value):
        time_field = self.wait.until(
                    EC.element_to_be_clickable(*self.WAIT_TIMER_FIELD)
                )
        time_field.click()
        time_field.clear()
        time_field.send_keys(field_value)

    def click_button(self, sequence):
        """Нажимает кнопки по очереди, как передано в sequence
        (список символов, например ['7', '+', '8', '=']"""
        for key in sequence:
            if key not in self.BUTTON_LOCATORS:
                raise ValueError(f"Неизвестный символ в последовательности: {key}")
            btn = self.wait.until(EC.element_to_be_clickable(
                *self.BUTTON_LOCATORS[key]))
            btn.click()

    def get_result(self):
        result = self.wait.until(EC.visibility_of_element_located(
            *self.RESULT_FIELD))
        return result.text
