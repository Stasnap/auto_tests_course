from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

brow = webdriver.Chrome()
link = ('http://suninjuly.github.io/selects1.html')


def calc(x1, x2):
    return str(x1 + x2)


try:
    brow.get(link)

    x1 = brow.find_element(By.ID, 'num1').text
    x2 = brow.find_element(By.ID, 'num2').text
    result = calc(int(x1), int(x2))
    print(result)
    brow.find_element(By.ID, 'dropdown').click()
    select = Select(brow.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(result))
    brow.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(10)
    brow.quit()


