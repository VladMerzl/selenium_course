import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")

    browser.find_element(By.NAME, "first_name").send_keys("John")
    browser.find_element(By.NAME, "last_name").send_keys("Doe")
    browser.find_element(By.CLASS_NAME, "city").send_keys("Boston")
    browser.find_element(By.ID, "country").send_keys("United States")

    browser.find_element(By.XPATH, "//div[@class='container']/form[@method='get']/div[6]/button[@type='submit']").click()

finally:
    time.sleep(5)
    browser.quit()

