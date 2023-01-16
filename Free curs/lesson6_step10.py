from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link_old = ('http://suninjuly.github.io/registration1.html')
link = ('http://suninjuly.github.io/registration2.html')
brow = webdriver.Chrome()

try:
    brow.get(link)  # переходим по ссылке

    brow.find_element(  # находим и заполняем первое обязательное поле
        By.CSS_SELECTOR, 'input[placeholder="Input your first name"]'
    ).send_keys('Pickle')

    brow.find_element(  # находим и заполняем второе обязательное поле
        By.CSS_SELECTOR, 'input[placeholder="Input your last name"]'
    ).send_keys('Pickleeni')

    brow.find_element(  # находим и заполняем третье обязательное поле
        By.CSS_SELECTOR, 'input[placeholder="Input your email"]'
    ).send_keys('Pickleeni@mail.ru')

    time.sleep(3)

    brow.find_element(  # находим и жмякаем кнопку
        By.CSS_SELECTOR, 'button.btn'
    ).click()

    time.sleep(1)

    text_welc = brow.find_element(By.TAG_NAME, 'h1').text

    if "Congratulations! You have successfully registered!" == text_welc:
        print('Test pass')
    else:
        print('Error')

finally:
    time.sleep(10)
    brow.quit()
