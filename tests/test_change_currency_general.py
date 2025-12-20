from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_change_currency_general(browser):
    browser.get(f'{browser.base_url}')

    wait = WebDriverWait(browser, 3)

    active_currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".expand-more"))).text
    price_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".price"))).text

    new_currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".expand-more._gray-darker")))
    new_currency.click()

    new_currency = wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[text()='USD $']")))
    new_currency.click()

    active_currency_new = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".expand-more"))).text
    assert active_currency_new != active_currency, "Currency did not change"

    new_price_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".price"))).text


