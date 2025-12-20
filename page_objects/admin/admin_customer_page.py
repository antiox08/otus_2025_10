from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class AdminCustomerPage(BasePage):

    def wait_page_basket(self) -> None:
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-danger"))
        )

    def click_basket(self) -> None:
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-danger"))
        ).click()
    def page_add_customers(self) -> None:
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='customer.form']"))
        ).click()

    def click_checkbox(self) -> None:
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table input[type='checkbox']"))
        ).click()

    def wait_user_in_list(self, first_name: str, last_name: str) -> None:
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                f"//table//tr[td[text()='{first_name}'] and td[text()='{last_name}']]"
            ))
        )