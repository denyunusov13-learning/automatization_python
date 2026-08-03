from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_Page:

    USERNAME_FIELD = (By.ID, "user-name")
    PASS_FIELD = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self):
        username_field = self.wait.until(
            EC.element_to_be_clickable(self.USERNAME_FIELD))
        username_field.clear()
        username_field.send_keys("standard_user")
        pass_field = self.driver.find_element(*self.PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys("secret_sauce")
        login_button = self.driver.find_element(*self.SUBMIT_BUTTON)
        login_button.click()
