from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Checkout_Page:

    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POST_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_PRICE_VALUE = (By.CSS_SELECTOR, "div[data-test='total-label']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_first_name_field(self):
        firstname_field = self.wait.until(EC.element_to_be_clickable(
                self.FIRST_NAME_FIELD))
        firstname_field.clear()
        firstname_field.send_keys("Денис")

    def fill_last_name_field(self):
        lastname_field = self.driver.find_element(*self.LAST_NAME_FIELD)
        lastname_field.clear()
        lastname_field.send_keys("Юнусов")

    def fill_post_code_field(self):
        post_code_field = self.driver.find_element(*self.POST_CODE_FIELD)
        post_code_field.clear()
        post_code_field.send_keys("633456")

    def click_continue_btn(self):
        continue_btn = self.driver.find_element(*self.CONTINUE_BUTTON)
        continue_btn.click()

    def get_total_price_value(self):
        total_price_value = self.wait.until(EC.visibility_of_element_located(
                self.TOTAL_PRICE_VALUE))
        self.driver.execute_script(
            "arguments[0].scrollIntoView();", total_price_value)
        return total_price_value.text
