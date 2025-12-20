from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage
import time
from log.logger import get_logger
import allure


logger = get_logger()
class AdminAddProductPage(BasePage):

    def add_product(self) -> None:
        """Создание товара"""
        with allure.step("Создание нового товара"):
            logger.info("Создание нового товара")

        category_name = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#input-name-1")))
        category_name.clear()
        category_name.send_keys("Test")

        meta_name = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#input-meta-title-1")))
        meta_name.clear()
        meta_name.send_keys("Test")

    def add_model(self, keyword: str = None) -> None:
        """Добавить Model"""

        # Кликаем на вкладку Data
        WebDriverWait(self.browser, 2).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Data"))
        ).click()

        # Ждем, пока поле Model станет видимым
        model_name = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located((By.ID, "input-model"))
        )
        model_name.clear()
        model_name.send_keys("test")

    def add_seo(self, keyword: str = None) -> None:
        """Добавить SEO"""

        # Если keyword не передан, генерируем уникальный
        if keyword is None:
            timestamp = int(time.time())
            keyword = f"test-product-{timestamp}"

        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, "SEO"))).click()

        seo_name = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#input-keyword-0-1")))
        seo_name.clear()
        seo_name.send_keys(keyword)

    def save_product(self) -> None:
        """Сохранение товара"""
        with allure.step("Сохранение товара"):
            logger.info("Сохранение товара")

        WebDriverWait(self.browser, 5).until(
             EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary"))).click()

    def return_to_product_list(self) -> None:
        """Вернуться к списку товара"""

        WebDriverWait(self.browser, 5).until(
             EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-light"))).click()
