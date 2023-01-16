from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = ('http://suninjuly.github.io/redirect_accept.html')

with webdriver.Chrome() as brow:
    brow.get(link)
    time.sleep(5)
    brow.find_element(By.CSS_SELECTOR, 'button.trollface').click()

    window2 = brow.window_handles[1]
    window1 = brow.window_handles[0]
    brow.switch_to.window(window2)

    num = brow.find_element(By.ID, 'input_value').text
    x = calc(num)

    brow.find_element(By.ID, 'answer').send_keys(x)
    brow.find_element(By.TAG_NAME, 'button').click()
    time.sleep(2)

    print(brow.switch_to.alert.text)


