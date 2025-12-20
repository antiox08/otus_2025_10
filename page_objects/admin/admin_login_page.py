from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage
import time
from log.logger import get_logger
import allure


logger = get_logger()
class AdminLoginPage(BasePage):

    def wait_login_page(self):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.ID, "input-username"))
        )

    def login(self, username: str, password: str):

        with allure.step("Ввод логина и пароля в админке"):
            logger.info("Ввод логина и пароля в админке")

        self.wait_login_page()
        self.browser.find_element(By.ID, "input-username").send_keys(username)
        self.browser.find_element(By.ID, "input-password").send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def wait_logged_in(self, timeout: int = 10):
        with allure.step("Ожидание успешного логина"):
            logger.info("Ожидание успешного логина")

        WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located((By.ID, "menu-dashboard"))
        )
