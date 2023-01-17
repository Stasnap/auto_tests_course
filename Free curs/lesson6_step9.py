from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = ('http://suninjuly.github.io/registration1.html')
brow = webdriver.Chrome()

try:
    brow.get(link)

    for i in brow.find_elements(By.CSS_SELECTOR, 'div.first_block input'):
        i.send_keys('Kick')
    # for n in brow.find_elements(By.CSS_SELECTOR, 'div.second_block input'):
    #     n.send_keys('you')
    brow.find_element(By.CSS_SELECTOR, 'button.btn').click()
    time.sleep(1)

    text_welc = brow.find_element(By.TAG_NAME, 'h1').text

    if "Congratulations! You have successfully registered!" == text_welc:
        print('Test pass')
    else:
        print('Bag detected or Error code')

finally:
    time.sleep(10)
    brow.quit()
