from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("Лариса")
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("Викторовна")
    browser.find_element(By.CSS_SELECTOR, "input[class$='third']").send_keys("a@norbit.ru")
    browser.find_element(By.CSS_SELECTOR, "button[class$='btn-default']").click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(10)
    browser.quit()
    
try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("Лариса")
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("Викторовна")
    browser.find_element(By.CSS_SELECTOR, "input[class$='third']").send_keys("a@norbit.ru")
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your phone']").send_keys("89102100017")
    browser.find_element(By.CSS_SELECTOR, "button[class$='btn-default']").click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
