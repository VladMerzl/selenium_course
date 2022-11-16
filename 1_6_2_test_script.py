from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://google.com/")

search_field = browser.find_element(By.CSS_SELECTOR, '[title="Поиск"]')
search_field.send_keys('Что такое автотесты')
browser.find_element_by_name('btnK').click()

browser.quit()

