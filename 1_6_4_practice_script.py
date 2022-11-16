import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/simple_form_find_task.html")

    browser.find_element(By.NAME, "first_name").send_keys("John")
    browser.find_element(By.NAME, "last_name").send_keys("Doe")
    browser.find_element(By.CLASS_NAME, "city").send_keys("Boston")
    browser.find_element(By.ID, "country").send_keys("United States")

    browser.find_element(By.ID, "submit_button").click()

finally:
    time.sleep(30)
    browser.quit()

