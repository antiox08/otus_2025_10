from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage


class ComparisonPage(BasePage):

    def wait_for_product_in_comparison(self, product_name: str):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.LINK_TEXT, product_name))
        )

    def click_confirm(self):
        from selenium.webdriver.common.by import By

        element = self.browser.find_element(By.CSS_SELECTOR, "#button-confirm")

        self.browser.execute_script("arguments[0].click();", element)
