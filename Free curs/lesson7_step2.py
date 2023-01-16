from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


brow = webdriver.Chrome()
link = ('http://suninjuly.github.io/get_attribute.html')

try:
    brow.get(link)

    x_element = brow.find_element(By.CSS_SELECTOR, "img").get_attribute("valuex")
    x = calc(x_element)

    brow.find_element(By.ID, 'answer').send_keys(x)
    brow.find_element(By.ID, 'robotCheckbox').click()
    brow.find_element(By.ID, 'robotsRule').click()
    brow.find_element(By.CSS_SELECTOR, 'button.btn').click()
    time.sleep(1)


finally:
    time.sleep(10)
    brow.quit()
