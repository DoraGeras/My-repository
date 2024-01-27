import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
driver.get("https://SunInJuly.github.io/execute_script.html")
num = driver.find_element(By.CSS_SELECTOR, "span[id='input_value']").text
x = calc(num)
driver.execute_script("arguments[0].scrollIntoView();",driver.find_element(By.CSS_SELECTOR, "input[id='answer']"))
driver.find_element(By.CSS_SELECTOR, "input[id='answer']").send_keys(x)
driver.find_element(By.CSS_SELECTOR, "input[id='robotCheckbox']").click()
driver.execute_script("arguments[0].scrollIntoView();",driver.find_element(By.CSS_SELECTOR, "input[id='robotsRule']"))
driver.find_element(By.CSS_SELECTOR, "input[id='robotsRule']").click()
driver.find_element(By.XPATH, "//*[text() = 'Submit']").click()
time.sleep(10)



