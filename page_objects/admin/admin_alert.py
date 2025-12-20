import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertSuccessElement:

    def __init__(self, browser):
        self.browser = browser

    def _wait(self):
        """Ожидание успешного сообщения"""
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
        )

    def confirm_alert(self):
        """Подтвердить alert"""
        # Ждем alert
        time.sleep(1)

        # Переключаемся на alert
        alert = self.browser.switch_to.alert

        # Получаем текст
        alert_text = alert.text
        print(f"Текст alert: {alert_text}")

        # Подтверждаем
        alert.accept()

        # Возвращаемся к основному контенту
        self.browser.switch_to.default_content()
