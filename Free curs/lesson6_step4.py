from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = ('http://suninjuly.github.io/find_link_text')

with webdriver.Chrome() as browser:
    browser.get(link)

    browser.find_element(By.LINK_TEXT, '224592').click()
    browser.find_element(By.TAG_NAME, 'input').send_keys("Ivan")
    browser.find_element(By.NAME, 'last_name').send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, 'form-control.city').send_keys("Smolensk")
    browser.find_element(By.ID, "country").send_keys("Russia")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(15)
