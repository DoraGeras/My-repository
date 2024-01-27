from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
try:
    driver.get('http://suninjuly.github.io/explicit_wait2.html')
    WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    driver.find_element(By.ID, 'book').click()
    y = calc(int(driver.find_element(By.ID, 'input_value').text))
    driver.find_element(By.ID, 'answer').send_keys(str(y))
    driver.find_element(By.ID, 'solve').click()
    sleep(30)
finally:
    driver.quit()
    