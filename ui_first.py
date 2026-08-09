import time
from selenium import webdriver

# Современный способ. Selenium Manager автоматически настроит драйвер
driver = webdriver.Chrome()

# Открываем страницу
driver.get("https://www.google.com")

# Ждем 10 секунд (чтобы увидеть результат)
time.sleep(10)

# Закрываем браузер
driver.quit()
