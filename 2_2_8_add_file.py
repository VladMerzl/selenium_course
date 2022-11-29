import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    browser.find_element(By.CSS_SELECTOR, "[name=firstname]").send_keys("John")
    browser.find_element(By.CSS_SELECTOR, "[name=lastname]").send_keys("Doe")
    browser.find_element(By.CSS_SELECTOR, "[name=email]").send_keys("jdoe@mail.test")

    current_dir = os.path.abspath(os.path.dirname("c:/selenium_course/"))
    filepath = os.path.join(current_dir, "2_2_8_file.txt")

    browser.find_element(By.ID, "file").send_keys(filepath)

    browser.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(3)
    browser.quit()