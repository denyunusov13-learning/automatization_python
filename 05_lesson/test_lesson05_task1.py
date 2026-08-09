import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_lesson05_task1():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/")
    driver.maximize_window()
    first_url = driver.current_url

    time.sleep(8)

    html_form_button = driver.find_element(By.LINK_TEXT, "HTML form")
    html_form_button.click()

    time.sleep(5)
    new_url = driver.current_url
    assert new_url != first_url

    driver.back()
    time.sleep(5)
    old_url = driver.current_url
    assert old_url == first_url

    driver.quit()
