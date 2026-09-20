import pytest
from selenium import webdriver


@pytest.fixture

def setup():
    driver = webdriver.Chrome()
    print(f"webdriver initialized: {driver}")
    driver.maximize_window()
    print(f"webdriver maximized")
    yield driver
    driver.quit()
    print(f"webdriver closed")
