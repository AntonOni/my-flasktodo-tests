import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def driver_setup(request):
    chrome = webdriver.Chrome(ChromeDriverManager().install())
    chrome.maximize_window()
    chrome.get("http://ec2-54-167-34-122.compute-1.amazonaws.com:5000/")
    chrome.implicitly_wait(10)
    request.cls.chrome = chrome
    yield
    chrome.close()