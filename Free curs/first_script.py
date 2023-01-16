import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as brow:
    brow.get("https://suninjuly.github.io/text_input_task.html")
    brow.find_element(By.CSS_SELECTOR, '.textarea').send_keys('get()')

    brow.find_element(By.CSS_SELECTOR, '.submit-submission').click()
    time.sleep(5)
