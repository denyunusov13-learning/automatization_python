from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    start_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Start']")))
    start_button.click()

    text_content = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h4[normalize-space()='Hello World!']")))
    driver.save_screenshot("06_lesson/full_screen.png")

    text_content = driver.find_element(
        By.XPATH, "//h4[normalize-space()='Hello World!']")
    assert text_content.text == "Hello World!"

    driver.quit()
