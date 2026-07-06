import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_lesson05_task3():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")
    driver.maximize_window()

    time.sleep(2)

    html_form = driver.find_elements(By.TAG_NAME, "a")
    assert len(html_form) == 9

    list_html_form = [element for element in html_form
                      if element.is_displayed()]
    assert len(list_html_form) == 9
    assert "1" in list_html_form[0].text

    driver.quit()
