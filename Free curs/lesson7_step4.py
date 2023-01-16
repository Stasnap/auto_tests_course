from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


brow = webdriver.Chrome()
link = ('http://suninjuly.github.io/execute_script.html')

try:
    brow.get(link)

    x_element = brow.find_element(By.ID, 'input_value').text
    x = calc(x_element)

    brow.find_element(By.ID, 'answer').send_keys(x)
    button = brow.find_element(By.CSS_SELECTOR, 'button.btn')
    brow.execute_script("return arguments[0].scrollIntoView(true);", button)
    brow.find_element(By.ID, 'robotCheckbox').click()
    brow.find_element(By.ID, 'robotsRule').click()
    brow.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(10)
    brow.quit()
