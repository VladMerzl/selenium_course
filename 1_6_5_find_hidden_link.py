import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_link_text")

    value1 = str(math.ceil(math.pow(math.pi, math.e)*10000))
    browser.find_element(By.LINK_TEXT, value1).click()

    browser.find_element(By.NAME, "first_name").send_keys("John")
    browser.find_element(By.NAME, "last_name").send_keys("Doe")
    browser.find_element(By.CLASS_NAME, "city").send_keys("Boston")
    browser.find_element(By.ID, "country").send_keys("United States")

    browser.find_element(By.CLASS_NAME, "btn").click()

finally:
    time.sleep(10)
    browser.quit()

