from selenium import webdriver
from selenium.webdriver.common.by import By

link = ('http://suninjuly.github.io/wait1.html')

with webdriver.Chrome() as brow:
    brow.implicitly_wait(5)
    brow.get(link)
    brow.find_element(By.ID, 'verify').click()

    assert 'successful' in brow.find_element(By.ID, 'verify_message').text
