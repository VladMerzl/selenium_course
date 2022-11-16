

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    value = 0
    elements = browser.find_elements(By.CSS_SELECTOR, "[type=text]")
    for element in elements:
        element.send_keys(value)
        value += 1

    browser.find_element(By.CLASS_NAME, "btn").click()

finally:
    time.sleep(10)
    browser.quit()
