from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterPage(BasePage):

    URL = "https://test-automation.kartala.dev/register"

    NAME_INPUT = (By.ID, "name-field")
    EMAIL_INPUT = (By.ID, "email-field")
    PHONE_INPUT = (By.ID, "phone-field")
    PASSWORD_INPUT = (By.ID, "password-field")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-primary")

    def open(self):
        self.driver.get(self.URL)

    def register(self, name, email, phone, password):
        self.type(self.NAME_INPUT, name)
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PHONE_INPUT, phone)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.REGISTER_BUTTON)

    def get_validation_message(self, locator):
        element = self.driver.find_element(*locator)
        return self.driver.execute_script(
            "return arguments[0].validationMessage;", element
        )

    def is_redirect_to_login(self):
        """
        Mengecek apakah user diarahkan ke halaman login setelah registrasi sukses.
        """
        return self.driver.current_url.endswith("/login")
