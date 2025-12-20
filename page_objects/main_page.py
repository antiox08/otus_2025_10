from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = browser.base_url

    def open(self):
        """Открытие главной страницы"""
        self.browser.get(self.url)

    def click_featured_product(self, index: int = 0) -> str:
        import time

        time.sleep(1)

        products = self.browser.find_elements(By.CSS_SELECTOR, ".description")

        product_name = products[index].find_element(By.CSS_SELECTOR, "h4 a").text

        # Скролл с помощью JavaScript
        link = products[index].find_element(By.CSS_SELECTOR, "h4 a")
        self.browser.execute_script("arguments[0].click();", link)

        time.sleep(1)

        return product_name
