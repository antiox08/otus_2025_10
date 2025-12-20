from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ProductPage(BasePage):

    def add_to_cart(self) -> None:
        """Добавление в корзину"""
        self.browser.find_element(By.CSS_SELECTOR, "#button-cart").click()

    def add_to_comparison(self) -> None:
        """Добавление в сравнение"""
        self.browser.find_element(By.CSS_SELECTOR, "[title='Compare this Product']").click()

    def add_to_wish_list(self) -> None:
        """Добавление в избранное"""
        self.browser.find_element(By.CSS_SELECTOR, "[title='Add to Wish List']").click()
