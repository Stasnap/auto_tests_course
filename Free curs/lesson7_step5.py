from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

brow = webdriver.Chrome()
link = ('http://suninjuly.github.io/file_input.html')

try:
    brow.get(link)

    brow.find_element(By.NAME, "firstname").send_keys('Pickle')
    brow.find_element(By.NAME, "lastname").send_keys('Pickleni')
    brow.find_element(By.NAME, "email").send_keys('Pickle@mail.ru')

    file_element = brow.find_element(By.ID, 'file')           # находим элемент
    current_dir = os.path.abspath(os.path.dirname(__file__))  # текущая директория
    file_path = os.path.join(current_dir, 'file.txt')         # добавляем имя файла к пути
    file_element.send_keys(file_path)                         # отправляем

    brow.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(10)
    brow.quit()

