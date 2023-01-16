import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC

link = ('https://yandex.ru/maps/46/kirov/?ll=49.671105%2C58.598554&z=13')

with webdriver.Chrome() as brow:
    brow.get(link)
    brow.implicitly_wait(5)
    brow.find_element(
        By.XPATH,
        '/html/body/div[1]/div[2]/div[2]/header/div/div/div/form/div[2]/div/span/span/input'
    ).send_keys('Стоматологическая клиника')

    brow.find_element(By.CSS_SELECTOR, 'button[aria-label="Найти"]').click()

    list_search = brow.find_elements(
        By.CSS_SELECTOR, 'ul.search-list-view__list'
    )


    time.sleep(10)