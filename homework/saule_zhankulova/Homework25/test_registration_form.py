import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


FORM_URL = "https://demoqa.com/automation-practice-form"

FORM_DATA = {
    "first_name": "Alex",
    "last_name": "Ivanov",
    "email": "alex.ivanov@example.com",
    "gender": "Male",
    "mobile": "7900123456",
    "date_of_birth": "15 May 1995",
    "date_of_birth_result": "15 May,1995",
    "subjects": ["Maths", "Computer Science"],
    "hobbies": ["Sports", "Reading"],
    "address": "10 Test Street, Astrakhan",
    "state": "NCR",
    "city": "Delhi",
}


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=700,900")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(2)
    yield browser
    browser.quit()


class TestDemoQAForm:
    def test_fill_practice_form_and_print_result(self, driver):
        wait = WebDriverWait(driver, 15)
        driver.get(FORM_URL)

        self._fill_text_field(driver, "firstName", FORM_DATA["first_name"])
        self._fill_text_field(driver, "lastName", FORM_DATA["last_name"])
        self._fill_text_field(driver, "userEmail", FORM_DATA["email"])
        self._click_label(driver, FORM_DATA["gender"])
        self._fill_text_field(driver, "userNumber", FORM_DATA["mobile"])
        self._set_date_of_birth(driver, FORM_DATA["date_of_birth"])

        for subject in FORM_DATA["subjects"]:
            self._select_autocomplete_value(driver, "subjectsInput", subject)

        for hobby in FORM_DATA["hobbies"]:
            self._click_label(driver, hobby)

        self._fill_text_field(driver, "currentAddress", FORM_DATA["address"])
        self._select_dropdown_value(driver, "state", FORM_DATA["state"])
        self._select_dropdown_value(driver, "city", FORM_DATA["city"])

        self._scroll_into_view(driver, driver.find_element(By.ID, "submit"))
        self._safe_click(driver, driver.find_element(By.ID, "submit"))

        modal = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
        result = self._get_modal_result(modal)
        print(result)

        assert result["Student Name"] == f"{FORM_DATA['first_name']} {FORM_DATA['last_name']}"
        assert result["Student Email"] == FORM_DATA["email"]
        assert result["Gender"] == FORM_DATA["gender"]
        assert result["Mobile"] == FORM_DATA["mobile"]
        assert result["Date of Birth"] == FORM_DATA["date_of_birth_result"]
        assert result["Subjects"] == ", ".join(FORM_DATA["subjects"])
        assert result["Hobbies"] == ", ".join(FORM_DATA["hobbies"])
        assert result["Address"] == FORM_DATA["address"]
        assert result["State and City"] == f"{FORM_DATA['state']} {FORM_DATA['city']}"


    @staticmethod
    def _scroll_into_view(driver, element):
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def _safe_click(self, driver, element):
        self._scroll_into_view(driver, element)
        try:
            element.click()
        except Exception:
            driver.execute_script("arguments[0].click();", element)

    def _fill_text_field(self, driver, element_id, value):
        field = driver.find_element(By.ID, element_id)
        self._scroll_into_view(driver, field)
        field.clear()
        field.send_keys(value)

    def _click_label(self, driver, label_text):
        label = driver.find_element(By.XPATH, f"//label[normalize-space()='{label_text}']")
        self._safe_click(driver, label)

    def _set_date_of_birth(self, driver, date_value):
        field = driver.find_element(By.ID, "dateOfBirthInput")
        self._safe_click(driver, field)
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(date_value)
        field.send_keys(Keys.ENTER)

    def _select_autocomplete_value(self, driver, element_id, value):
        field = driver.find_element(By.ID, element_id)
        self._scroll_into_view(driver, field)
        field.send_keys(value)
        field.send_keys(Keys.ENTER)

    def _select_dropdown_value(self, driver, dropdown_id, value):
        wait = WebDriverWait(driver, 10)
        dropdown = wait.until(ec.element_to_be_clickable((By.ID, dropdown_id)))
        self._safe_click(driver, dropdown)
        input_field = dropdown.find_element(By.CSS_SELECTOR, "input")
        input_field.send_keys(value)
        option = wait.until(
            ec.element_to_be_clickable(
                (By.XPATH, f"//div[contains(@class, 'option') and normalize-space()='{value}']")
            )
        )
        self._safe_click(driver, option)

    @staticmethod
    def _get_modal_result(modal):
        rows = modal.find_elements(By.CSS_SELECTOR, "tbody tr")
        return {
            row.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text: row.find_element(
                By.CSS_SELECTOR, "td:nth-child(2)"
            ).text
            for row in rows
        }
