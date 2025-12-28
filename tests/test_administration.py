from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_administration_login_page(browser):
    browser.get(f"{browser.base_url}/administration")

    wait = WebDriverWait(browser, 3)
    field_email = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#email"))
    )
    field_password = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#passwd"))
    )
    submit_login = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#submit_login"))
    )
    chk_box_btn = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".md-checkbox"))
    )
    forgot_password_link = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#forgot-password-link")
        )
    )
