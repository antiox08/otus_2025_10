from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage
import time


class AdminMenuPage(BasePage):

    def click_to_catalog_product(self) -> None:
        """Переход на страницу редактирования каталога товаров"""

        WebDriverWait(self.browser, 1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu-catalog a[href='#collapse-1']"))
        ).click()


        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu-catalog a[href*='product']"))
        ).click()

    def click_to_customers(self) -> None:
        """Переход на страницу редактирования клиентов"""

        WebDriverWait(self.browser, 1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu-customer a[href='#collapse-5']"))
        ).click()

        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu-customer a[href*='customer']"))
        ).click()

    def wait_page_basket(self) -> None:
        """Ожидание, что пользователь перешёл на страницу"""
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-danger"))
        )