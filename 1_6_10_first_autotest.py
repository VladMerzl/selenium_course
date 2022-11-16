import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")
    success = "Congratulations! You have successfully registered!"

    browser.find_element(By.XPATH, "//div[@class='first_block']/div/input[@class='form-control first']").send_keys("John")
    browser.find_element(By.XPATH, "//div[@class='first_block']/div/input[@class='form-control second']").send_keys("Doe")
    browser.find_element(By.XPATH, "//div[@class='first_block']/div/input[@class='form-control third']").send_keys("test@testmail.tt")

    browser.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(2)

    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert success == welcome_text

finally:
    time.sleep(5)
    browser.quit()