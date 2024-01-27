import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/selects1.html")
num1 = driver.find_element(By.CSS_SELECTOR, "span[id='num1']").text
num2 = driver.find_element(By.CSS_SELECTOR, "span[id='num2']").text
suma = str(int(num1)+int(num2))
select = Select(driver.find_element(By.CSS_SELECTOR, "select[id='dropdown']"))
select.select_by_value(suma)
driver.find_element(By.XPATH, "//*[text() = 'Submit']").click()
time.sleep(10)



