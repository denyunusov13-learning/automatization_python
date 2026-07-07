from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "YTEyOTY3NDYtZGJkYy00NWY0LWEzMjAtYmY1MDFjYjY2OTJm",
        "domain": "gitflic.ru"
    })

    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    driver.refresh()

    personal_accaunt = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href='/user/yunusova_natasha']")))
    personal_accaunt.click()

    first_url = driver.current_url

    driver.delete_all_cookies()
    driver.refresh()

    driver.add_cookie({
        "name": "SESSION",
        "value": "ZDljMWVjMzQtNzQ5Ny00MjEzLWEwZjctOWU4ZGYyMjhjOTMw",
        "domain": "gitflic.ru"
    })

    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    driver.refresh()

    personal_accaunt = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href='/user/yunusov_denis']")))
    personal_accaunt.click()

    second_url = driver.current_url
    assert first_url != second_url

    driver.quit()
