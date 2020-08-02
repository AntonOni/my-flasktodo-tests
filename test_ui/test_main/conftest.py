import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def driver_setup(request):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    # chrome = webdriver.Chrome(ChromeDriverManager().install())
    # chrome.maximize_window()
    chrome.get("http://0.0.0.0:5000")
    chrome.implicitly_wait(10)
    request.cls.chrome = chrome
    yield
    chrome.close()
