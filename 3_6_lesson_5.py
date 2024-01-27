import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.parametrize("link", [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])
def test_feedback_text(browser, link):
    answer = str(math.log(int(time.time())))
    browser.get(link)
    browser.implicitly_wait(5)  # Увеличиваем время ожидания до 10 секунд


    # Ожидаем загрузки страницы после входа
    WebDriverWait(browser, 5).until(
        EC.url_contains("lesson")
    )

    # Вводим ответ и отправляем его
    text_area = browser.find_element(By.CSS_SELECTOR, ".textarea")
    text_area.send_keys(answer)
    submit_button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    submit_button.click()

    # Нажимаем кнопку войти
    login_button = browser.find_element(By.CSS_SELECTOR, "ember-view.light-tabs__switch")
    login_button.click()

    # Вводим логин и пароль
    login = "gerasimova.d4ri@yandex.ru"
    password = "Geras0310"
    login_input = browser.find_element(By.ID, "id_login_email")
    password_input = browser.find_element(By.ID, "id_login_password")
    login_input.send_keys(login)
    password_input.send_keys(password)

    # Ожидаем появления фидбека
    feedback = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    )
    assert feedback.text == "Correct!", f"Expected 'Correct!', but got '{feedback.text}'"
