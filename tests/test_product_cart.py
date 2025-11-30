from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_pc_page(browser):
    browser.get(f'{browser.base_url}/2-9-brown-bear-printed-sweater.html#/1-size-s')

    wait = WebDriverWait(browser, 3)
    name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".h1")))
    discount = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-discount")))
    current_price = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".current-price")))
    product_cover = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-cover")))
    add_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary.add-to-cart")))