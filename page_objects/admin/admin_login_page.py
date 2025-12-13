from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage
import time


class AdminLoginPage(BasePage):

    def wait_login_page(self):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.ID, "input-username"))
        )

    def login(self, username: str, password: str):
        self.wait_login_page()
        self.browser.find_element(By.ID, "input-username").send_keys(username)
        self.browser.find_element(By.ID, "input-password").send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def wait_logged_in(self, timeout: int = 10):
        WebDriverWait(self.browser, timeout).until(
            EC.url_contains("user_token=")
        )
