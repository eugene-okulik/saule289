from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_task1(driver):
    driver.get("http://testshop.qa-practice.com/")
    desk = driver.find_element(By.LINK_TEXT, "Customizable Desk")
    ActionChains(driver).key_down(Keys.CONTROL).click(desk).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles

    driver.switch_to.window(tabs[1])
    add_to_cart = driver.find_element(By.ID, "add_to_cart")
    add_to_cart.click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content'))
    )
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-secondary'))
    ).click()
    driver.implicitly_wait(10)

    driver.close()
    driver.switch_to.window(tabs[0])
    shop_cart = driver.find_element(By.CSS_SELECTOR, "a[aria-label='eCommerce cart']")
    shop_cart.click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "cart_products"))
    )
    cart_products = driver.find_element(By.ID, "cart_products")
    cart_item = cart_products.find_element(
        By.XPATH, ".//h6[contains(text(), 'Customizable Desk')]"
    )
    assert cart_item.is_displayed()


def test_task2(driver):
    driver.get("http://testshop.qa-practice.com/")
    product_image = driver.find_element(
        By.CSS_SELECTOR, "img[alt='Customizable Desk']"
    )
    actions = ActionChains(driver)
    actions.move_to_element(product_image).perform()
    add_to_cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a.btn.btn-primary.a-submit")
        )
    )
    add_to_cart.click()
    modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content'))
    )
    modal_text = modal.text
    assert "Customizable Desk" in modal_text
