from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_task1(driver):
    input_data = "123456"
    driver.get("https://www.qa-practice.com/elements/input/simple")
    text_string = driver.find_element(By.NAME, 'text_string')
    text_string.send_keys(input_data)
    text_string.submit()
    result_text = driver.find_element(By.ID, 'result-text')
    print(result_text.text)
    assert result_text.text == input_data
