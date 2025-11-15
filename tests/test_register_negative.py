import time
from pages.register_page import RegisterPage

def test_register_negative_short_name(driver):
    page = RegisterPage(driver)

    page.open()
    page.register(
        name="H",  # invalid
        email="wrong@example.com",
        phone="08123",
        password="abcdef"
    )

    # User harus tetap di halaman register
    assert page.driver.current_url.endswith("/register"), \
        "User tidak boleh redirect jika input tidak valid!"

# Tambahkan delay agar browser tidak langsung close
    time.sleep(5)