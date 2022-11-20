import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    treasure = browser.find_element(By.TAG_NAME, "img").get_attribute("valuex")
    answer = calc(treasure)

    browser.find_element(By.ID, "answer").send_keys(answer)

    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    time.sleep(1)

    browser.find_element(By.CSS_SELECTOR, "[type=submit]").click()

finally:
    time.sleep(5)
    browser.quit()