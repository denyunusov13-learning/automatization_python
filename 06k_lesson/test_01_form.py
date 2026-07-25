from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_alert():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    first_name_field = wait.until(
        EC.element_to_be_clickable((By.NAME, "first-name"))
    )
    first_name_field.clear()
    first_name_field.send_keys("Иван")

    last_name_field = driver.find_element(By.NAME, "last-name")
    last_name_field.clear()
    last_name_field.send_keys("Петров")

    address_field = driver.find_element(By.NAME, "address")
    address_field.clear()
    address_field.send_keys("Ленина, 55-3")

    email_field = driver.find_element(By.NAME, "e-mail")
    email_field.clear()
    email_field.send_keys("test@skypro.com")

    phone_field = driver.find_element(By.NAME, "phone")
    phone_field.clear()
    phone_field.send_keys("+7985899998787")

    zip_code_field = driver.find_element(By.NAME, "zip-code")
    zip_code_field.clear()

    city_field = driver.find_element(By.NAME, "city")
    city_field.clear()
    city_field.send_keys("Москва")

    country_field = driver.find_element(By.NAME, "country")
    country_field.clear()
    country_field.send_keys("Россия")

    job_position_field = driver.find_element(By.NAME, "job-position")
    job_position_field.clear()
    job_position_field.send_keys("QA")

    company_field = driver.find_element(By.NAME, "company")
    company_field.clear()
    company_field.send_keys("SkyPro")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    submit_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit'].btn-outline-primary"
    )
    submit_button.click()

    zip_code_alert = wait.until(EC.visibility_of_element_located(
        (By.ID, "zip-code")))
    assert "alert-danger" in zip_code_alert.get_attribute("class")

    success_fields = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company",
    ]

    for field_id in success_fields:
        field_alert = wait.until(EC.visibility_of_element_located((
            By.ID, field_id)))
        assert "alert-success" in field_alert.get_attribute("class")

    driver.quit()
