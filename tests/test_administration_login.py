from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_administration_login(browser):
    browser.get(f'{browser.base_url}/administration')

    wait = WebDriverWait(browser, 3)
    field_email = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#email")))
    field_password = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#passwd")))
    submit_login = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#submit_login")))

    field_email.send_keys('admin@example.com')
    field_password.send_keys('Admin123!')
    submit_login.click()

    my_avatar = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#employee_infos")))
    assert my_avatar.is_displayed(), 'Login failed'

    my_avatar = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#employee_infos"))).click()
    header_logout = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header_logout"))).click()

    submit_login = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#submit_login")))
    assert submit_login.is_displayed(), 'Logout failed'




