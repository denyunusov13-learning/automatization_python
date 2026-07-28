from selenium.webdriver.common.by import By


class Cart_Page:

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def checkout_click(self):
        checkout_btn = self.driver.find_element(*self.CHECKOUT_BUTTON)
        self.driver.execute_script(
            "arguments[0].scrollIntoView();", checkout_btn)
        checkout_btn.click()
