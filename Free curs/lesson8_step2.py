from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = ('http://suninjuly.github.io/wait2.html')

with webdriver.Chrome() as brow:
    brow.implicitly_wait(5)
    brow.get(link)

    butt = WebDriverWait(brow, 5).until(
        EC.element_to_be_clickable((By.ID, 'verify'))
    )
    butt.click()

    assert "successful" in brow.find_element(By.ID, 'verify_message').text
