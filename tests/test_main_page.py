from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser):
    browser.get(f'{browser.base_url}')

    wait = WebDriverWait(browser, 3)

    cart = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".material-icons.shopping-cart")))
    sign_in = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".user-info")))
    currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#currency-selector-label")))
    contact_us = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#contact-link")))
    search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#search_widget")))
