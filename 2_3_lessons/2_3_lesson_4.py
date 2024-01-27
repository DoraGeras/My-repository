from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
try:
    driver.get('http://suninjuly.github.io/alert_accept.html')
    driver.find_element(By.TAG_NAME, 'button').click()
    driver.switch_to.alert.accept()
    y = calc(int(driver.find_element(By.ID, 'input_value').text))
    driver.find_element(By.ID, 'answer').send_keys(str(y))
    driver.find_element(By.CLASS_NAME, 'btn-primary').click()
    sleep(30)
finally:
    driver.quit()
