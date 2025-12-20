from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage
import time
from log.logger import get_logger
import allure


logger = get_logger()
class AdminAddCustomerPage(BasePage):

    def add_customer(self) -> None:
        """Создание пользователя"""
        with allure.step("Создание нового пользователя"):
            logger.info("Создание нового пользователя")

        first_name = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#input-firstname")))
        first_name.clear()
        first_name.send_keys("Test")

        last_name = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#input-lastname")))
        last_name.clear()
        last_name.send_keys("Test")

        email = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#input-email")))
        email.clear()
        email.send_keys("test@mail.ru")

        password = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#input-password")))
        password.clear()
        password.send_keys("Test")

        confirm_password = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#input-confirm")))
        confirm_password.clear()
        confirm_password.send_keys("Test")


    def save_customer(self) -> None:
        """Сохранение пользователя"""
        with allure.step("Сохранение пользователя"):
            logger.info("Сохранение пользователя")

        WebDriverWait(self.browser, 5).until(
             EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary"))).click()

    def return_to_product_list(self) -> None:
        """Вернуться к списку пользователей"""

        WebDriverWait(self.browser, 5).until(
             EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-light"))).click()
