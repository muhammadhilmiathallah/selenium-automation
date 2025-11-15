import time
from pages.register_page import RegisterPage
from utils.faker_utils import generate_email


def test_register_happy_path(driver):
    page = RegisterPage(driver)

    page.open()
    page.register(
        name="Hilmi",
        email=generate_email(),
        phone="08123456789",
        password="abcdef"
    )

    assert page.is_redirect_to_login(), "User seharusnya diarahkan ke halaman login!"


# Tambahkan delay agar browser tidak langsung close
    time.sleep(5)