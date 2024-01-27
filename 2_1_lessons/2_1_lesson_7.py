import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/get_attribute.html")


#driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
#driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
#driver.find_element(By.CSS_SELECTOR, "#robotsRule").click()
#driver.find_element(By.XPATH, "//*[text() = 'Submit']").click()


x_element = driver.find_element(By.CSS_SELECTOR, "#treasure").get_attribute('valuex')
y = calc(x_element)
driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
driver.find_element(By.CSS_SELECTOR, "#robotsRule").click()
driver.find_element(By.XPATH, "//*[text() = 'Submit']").click()

time.sleep(10)