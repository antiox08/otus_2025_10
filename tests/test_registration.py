from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_registration_page(browser):
    browser.get(f'{browser.base_url}/registration')

    wait = WebDriverWait(browser, 3)
    field_firstname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#field-firstname")))
    field_lastname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#field-lastname")))
    field_email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#field-email")))
    field_password = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#field-password")))
    field_birthday = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#field-birthday")))
