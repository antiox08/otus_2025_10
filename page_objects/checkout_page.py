from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage


class CheckoutPage(BasePage):

    def click_login_page(self):
        self.browser.find_element(By.LINK_TEXT, "login page").click()

    def wait_page_load(self):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".btn.btn-primary")
            )
        )

    def wait_payment_form(self):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(
                (By.ID, "checkout-payment-method")
            )
        )
