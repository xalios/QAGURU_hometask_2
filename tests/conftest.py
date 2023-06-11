import pytest
from selenium import webdriver


@pytest.fixture()
def browser_chrome():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    driver.set_window_size(1920, 1080)

    yield driver
    driver.close()
