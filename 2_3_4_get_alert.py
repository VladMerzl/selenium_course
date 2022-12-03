import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    browser.find_element(By.CSS_SELECTOR, "[type=submit]").click()

    alert = browser.switch_to.alert
    alert.accept()

    time.sleep(2)

    xvalue = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(xvalue))

    browser.find_element(By.CSS_SELECTOR, "[type=submit]").click()
finally:
    time.sleep(3)
    browser.quit()