from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertSuccessElement:

    def __init__(self, browser):
        self.browser = browser

    def _wait(self):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
        )

    @property
    def login(self):
        self._wait()
        return self.browser.find_element(By.LINK_TEXT, "login")

    @property
    def comparison(self):
        self._wait()
        return self.browser.find_element(By.LINK_TEXT, "product comparison")

    @property
    def shoping_cart(self):
        self._wait()
        return self.browser.find_element(By.LINK_TEXT, "shopping cart")

    def shoping_cart_click(self):
        self.shoping_cart.click()
