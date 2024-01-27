from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class test_page(unittest.TestCase):
    def test_page1(self):
        link = "http://suninjuly.github.io/registration1.html"
        driver = webdriver.Chrome()
        driver.get(link)

        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("Мария")
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("Опа")
        driver.find_element(By.CSS_SELECTOR, "input[class$='third']").send_keys("a@norbit.ru")
        driver.find_element(By.CSS_SELECTOR, "button[class$='btn-default']").click()

        time.sleep(1)

        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text
        time.sleep(1)
        driver.quit()
    def test_page2(self):
        link = "http://suninjuly.github.io/registration2.html"
        driver = webdriver.Chrome()
        driver.get(link)

        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("Мария")
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("Опа")
        driver.find_element(By.CSS_SELECTOR, "input[class$='third']").send_keys("a@norbit.ru")
        driver.find_element(By.CSS_SELECTOR, "button[class$='btn-default']").click()

        time.sleep(1)

        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text
        time.sleep(1)
        driver.quit()

if __name__ == "__main__":
    test_page.test_page1()
    test_page.test_page2()