from selenium import webdriver


def test_dynamic_loading():
    driver = webdriver.Chrome()
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

    driver.get("https://gitflic.ru/user/yunusova_natasha")

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

    driver.get("https://gitflic.ru/user/yunusov_denis")

    second_url = driver.current_url
    assert first_url != second_url

    driver.quit()
