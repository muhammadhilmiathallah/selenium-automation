from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):

    URL = "https://test-automation.kartala.dev/login"

    EMAIL_INPUT = (By.ID, "email-field")
    PASSWORD_INPUT = (By.ID, "password-field")
    LOGIN_BUTTON = (By.ID, "login-btn")

    ERROR_ALERT = (By.CSS_SELECTOR, ".alert.alert-danger")

    def open(self):
        self.driver.get(self.URL)

    def login(self, email, password):
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def is_redirect_to_user_list(self):
        """Cek cepat apakah URL sudah mengarah ke /users"""
        return "/users" in self.driver.current_url

    def wait_until_dashboard(self):
        """Login sukses → tunggu redirect ke dashboard."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_to_be("https://test-automation.kartala.dev/")
            )
            return True
        except:
            return False

    def get_error_message(self):
        """Untuk negative test."""
        try:
            return self.get_text(self.ERROR_ALERT)
        except:
            return None
