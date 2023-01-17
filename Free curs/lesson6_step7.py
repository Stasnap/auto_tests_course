from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = ('http://suninjuly.github.io/huge_form.html')

with webdriver.Chrome() as brow:
    brow.get(link)
    elements = brow.find_elements(By.TAG_NAME, "input")

    for element in elements:
        element.send_keys("заполненно")

    brow.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(10)
