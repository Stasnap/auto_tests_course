from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


brow = webdriver.Chrome()
link = ('https://suninjuly.github.io/math.html')

try:
    brow.get(link)
    x = brow.find_element(By.CSS_SELECTOR, "span#input_value").text
    result = calc(x)

    brow.find_element(By.ID, 'answer').send_keys(result)
    brow.find_element(By.CSS_SELECTOR, 'label[for="robotCheckbox"]').click()
    brow.find_element(By.CSS_SELECTOR, 'label[for="robotsRule"]').click()
    brow.find_element(By.CSS_SELECTOR, 'button.btn').click()

    time.sleep(10)

finally:
    brow.quit()

