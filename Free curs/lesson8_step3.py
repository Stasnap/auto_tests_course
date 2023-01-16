import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = ('http://suninjuly.github.io/explicit_wait2.html')

with webdriver.Chrome() as brow:
    brow.get(link)

    if WebDriverWait(brow, 15).until(
            EC.text_to_be_present_in_element((By.ID, 'price'), "$100")
    ):
        brow.find_element(By.ID, 'book').click()
    '''нажимаем кнопку бук, когда цена будет 100$'''

    actions = AC(brow)
    actions.move_to_element(brow.find_element(By.ID, 'solve'))
    '''скролим страницу к нужному элементу'''

    result = brow.find_element(By.ID, 'input_value').text
    x = calc(result)
    '''находим число для формулы и вычисляем Х'''

    brow.find_element(By.ID, 'answer').send_keys(x)
    brow.find_element(By.ID, 'solve').click()

    print(brow.switch_to.alert.text)
