from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


brow = webdriver.Chrome()
link = ('http://suninjuly.github.io/alert_accept.html')

try:
    brow.get(link)
    brow.find_element(By.CSS_SELECTOR, 'button.btn').click()
    brow.switch_to.alert.accept()

    x = brow.find_element(By.ID, 'input_value').text
    (result) = calc(x)

    brow.find_element(By.ID, ('answer')).send_keys(result)
    brow.find_element(By.CSS_SELECTOR, 'button.btn').click()
    print(brow.switch_to.alert.text)

finally:
    brow.quit()
