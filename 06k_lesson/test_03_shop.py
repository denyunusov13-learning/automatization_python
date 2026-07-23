from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def success_purchase():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    username_field = wait.until(
            EC.element_to_be_clickable((By.ID, "user-name"))
        )
    username_field.clear()
    username_field.send_keys("standard_user")

    pass_field = driver.find_element(By.ID, "password")
    pass_field.clear()
    pass_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    backpack_btn = wait.until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-backpack")))
    backpack_btn.click()

    shirt_btn = driver.find_element(
        By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    driver.execute_script("arguments[0].scrollIntoView();", shirt_btn)
    shirt_btn.click()

    onesie_btn = driver.find_element(
        By.ID, "add-to-cart-sauce-labs-onesie")
    driver.execute_script("arguments[0].scrollIntoView();", onesie_btn)
    onesie_btn.click()

    cart_btn = driver.find_element(
            By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")
    driver.execute_script("arguments[0].scrollIntoView();", cart_btn)
    cart_btn.click()

    checkout_btn = driver.find_element(
            By.ID, "checkout")
    driver.execute_script("arguments[0].scrollIntoView();", checkout_btn)
    checkout_btn.click()

    firstname_field = wait.until(EC.element_to_be_clickable(
            (By.ID, "first-name")))
    firstname_field.clear()
    firstname_field.send_keys("Денис")

    lastname_field = driver.find_element(By.ID, "last-name")
    lastname_field.clear()
    lastname_field.send_keys("Юнусов")

    post_code_field = driver.find_element(By.ID, "postal-code")
    post_code_field.clear()
    post_code_field.send_keys("633456")

    continue_btn = driver.find_element(
            By.ID, "continue")
    continue_btn.click()

    total_price_value = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div[data-test='total-label']")))
    driver.execute_script("arguments[0].scrollIntoView();", total_price_value)
    total_price = total_price_value.text

    driver.quit()

    assert "$58.29" in total_price
