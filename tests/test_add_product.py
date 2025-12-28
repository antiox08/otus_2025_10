from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_add_product(browser):
    browser.get(f"{browser.base_url}")

    wait = WebDriverWait(browser, 3)

    prodcut_main = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".thumbnail-top"))
    ).click()
    prodcut_cart = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".add-to-cart"))
    ).click()
    modal_view = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary"))
    ).click()

    product_in_cart = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-image"))
    )
    assert product_in_cart.is_displayed(), "product was not added"
