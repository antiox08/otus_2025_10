from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_catalog_page(browser):
    browser.get(f'{browser.base_url}/3-clothes')

    wait = WebDriverWait(browser, 3)
    category = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".h1")))
    subcategory = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subcategory-heading")))
    block_categories = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".block-categories")))
    search_filters_brands = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#search_filters_brands")))
    search_filters_suppliers = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#search_filters_suppliers")))
