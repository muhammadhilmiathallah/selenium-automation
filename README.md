menginstall chromedriver, seleniumnya dan phyton nya
note(Tidak wajib install chromedriver.exe manual karena sudah dibuatkan depedency di drive.py jadi tinggal instal depedenccy nya saja)


Gunakan Python minimal versi 3.10+ (Saya menggunakan Versi 3.14)

Sudah ada requirement.txt untuk menginstall depedency nya
selenium
webdriver-manager
pytest
langsung aja di terminal instlall 

"pip install -r requirements.txt"

Atau install manual

"pip install selenium webdriver-manager pytest pytest-html"

untuk menjalan kan perintah

"pytest -v"

atau kalau mau cek satu satu

"pytest tests/test_login_negative.py" (tinggal ubah nama file di folder tests aja)
