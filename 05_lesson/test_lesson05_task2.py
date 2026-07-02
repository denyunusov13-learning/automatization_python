import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_lesson05_task2():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")
    driver.maximize_window()
    first_url = driver.current_url

    time.sleep(8)

    input_field = driver.find_element(By.NAME, "custname")
    input_field.send_keys("Денис")

    enter_button = driver.find_element(By.XPATH, '//button[.="Submit order"]')
    enter_button.click()

    time.sleep(5)

    new_url = driver.current_url
    assert new_url != first_url

    driver.quit()
