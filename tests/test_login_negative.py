import time
from pages.login_page import LoginPage

def test_login_invalid_credentials(driver):
    page = LoginPage(driver)

    page.open()
    page.login(
        email="salah@example.com",
        password="password_salah"
    )

    error = page.get_error_message()

    assert error is not None, "Error message seharusnya muncul!"
    assert "Invalid" in error or "error" in error.lower(), \
        "Pesan error tidak sesuai!"

# Tambahkan delay agar browser tidak langsung close
    time.sleep(5)