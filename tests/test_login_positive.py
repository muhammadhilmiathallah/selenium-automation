import time
from pages.login_page import LoginPage

def test_login_happy_path(driver):
    page = LoginPage(driver)

    page.open()
    page.login(email="hilmi@example.com", password="hilmi123")

    assert page.wait_until_dashboard(), \
        "User seharusnya diarahkan ke halaman dashboard!"


# Tambahkan delay agar browser tidak langsung close
    time.sleep(5)