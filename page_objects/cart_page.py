from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage


class CartPage(BasePage):

    def click_checkout(self) -> None:
        """Нажатие перейти к оформлению"""
        self.browser.find_element(By.LINK_TEXT, "Checkout").click()

    def wait_for_product_in_cart(self, product_name: str) -> None:
        """Ожидание товара в корзине"""
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.LINK_TEXT, product_name))
        )
