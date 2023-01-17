from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = ('http://suninjuly.github.io/find_xpath_form')

with webdriver.Chrome() as brow:
    brow.get(link)

    brow.find_element(By.TAG_NAME, 'input').send_keys('Pupa')
    brow.find_element(By.NAME, 'last_name').send_keys('Pupov')
    brow.find_element(By.CLASS_NAME, 'form-control.city').send_keys('Papupinsk')
    brow.find_element(By.ID, 'country').send_keys('Papupeted Fediration')
    brow.find_element(By.XPATH, '//button[@type="submit"]').click()

    time.sleep(5)
