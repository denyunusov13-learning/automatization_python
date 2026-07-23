from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 50)
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    time_field = wait.until(
            EC.element_to_be_clickable((By.ID, "delay"))
        )
    time_field.click()
    time_field.clear()
    time_field.send_keys("45")

    click_7 = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='7']")))
    click_7.click()

    btn_plus = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='+']")))
    btn_plus.click()

    btn_8 = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='8']")))
    btn_8.click()

    btn_equals = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='=']")))
    btn_equals.click()

    wait.until(EC.invisibility_of_element_located((By.ID, "spinner")))

    sum_result = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".screen")))
    assert sum_result.text == "15"

    driver.quit()
