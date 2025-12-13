from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage


class UserPage(BasePage):

    def login(self, username: str, password: str) -> None:
        """Логин пользователя"""
        self.browser.find_element(By.CSS_SELECTOR, "#input-email").send_keys(username)
        self.browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, "#form-login button").click()

    def wait_logged_in(self):
        """Ожидание, что пользователь залогинен"""
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Logout"))
        )

    def click_wish_list(self):
        """Переход в избранное из личного кабинета"""
        self.browser.find_element(By.LINK_TEXT, "Wish List").click()
