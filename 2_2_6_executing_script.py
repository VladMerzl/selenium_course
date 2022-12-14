import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(a):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")

    x = browser.find_element(By.ID, "input_value").text
    answer = str(calc(int(x)))
    button = browser.find_element(By.TAG_NAME, "button")

    browser.find_element(By.ID, "answer").send_keys(answer)
    browser.find_element(By.ID, "robotCheckbox").click()

    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.ID, "robotsRule").click()

    button.click()
finally:
    time.sleep(3)
    browser.quit()
