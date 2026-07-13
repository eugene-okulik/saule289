from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_task3(driver):
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    choose_language = driver.find_element(By.ID, 'id_choose_language')
    select = Select(choose_language)
    select.select_by_visible_text("Python")
    submit = driver.find_element(By.ID, 'submit-id-submit')
    submit.click()
    result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'result'))
    )
    assert "Python" in result.text


def test_task4(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    start_button = driver.find_element(By.XPATH, "//button[text()='Start']")
    start_button.click()

    result_text = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, 'finish'))
    )
    assert result_text.text == 'Hello World!'
