from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage
import time
from log.logger import get_logger
import allure

logger = get_logger()

class AdminProductPage(BasePage):

    def wait_page_basket(self) -> None:
        """Ожидание, что пользователь перешёл на страницу(отображение иконки корзина)"""
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-danger"))
        )

    def click_basket(self) -> None:
        """Ожидание, что пользователь перешёл на страницу(отображение иконки корзина)"""
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-danger"))
        ).click()
    def page_add_product(self) -> None:
        """Переход на страницу создания продукта"""

        with allure.step("Переход на страницу создания товара"):
            logger.info("Переход на страницу создания товара")

        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='product.form']"))
        ).click()

    def click_checkbox(self) -> None:
        """Выбор товара"""
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table input[type='checkbox']"))
        ).click()
