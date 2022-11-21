import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")

    element_a = browser.find_element(By.ID, "num1").text
    element_b = browser.find_element(By.ID, "num2").text
    sum = str(int(element_a) + int(element_b))

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(sum)

    browser.find_element(By.CSS_SELECTOR, "[type=submit]").click()
finally:
    time.sleep(10)
    browser.quit()
