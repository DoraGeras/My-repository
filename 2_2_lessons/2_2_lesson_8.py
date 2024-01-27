import time
import math
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir,'file.txt')
driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/file_input.html")
driver.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys('Андрей')
driver.execute_script("arguments[0].scrollIntoView();",driver.find_element(By.CSS_SELECTOR, "input[name='lastname']"))
driver.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys('Орлов')
driver.execute_script("arguments[0].scrollIntoView();",driver.find_element(By.CSS_SELECTOR, "input[name='email']"))
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys('Andrey.Orlov@noribt.ru')
driver.execute_script("arguments[0].scrollIntoView();",driver.find_element(By.CSS_SELECTOR, "input[id='file']"))
driver.find_element(By.CSS_SELECTOR, "input[id='file']").send_keys(file_path)
driver.find_element(By.XPATH, "//*[text() = 'Submit']").click()
time.sleep(10)
