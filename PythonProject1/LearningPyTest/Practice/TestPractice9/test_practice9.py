# Exercise 9
# Create a Selenium driver fixture in conftest.py.
# Requirements:
# Chrome opens
# ↓
# maximize window
# ↓
# yield driver
# ↓
# test executes
# ↓
# driver.quit()
#
# Create one test that opens:
#
# https://www.amazon.in
#
# and verifies the title.
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test(setup):
    driver = setup
    driver.get("https://amazon.in")
    wait = WebDriverWait(driver, 10)
    logo_text = wait.until(
        EC.presence_of_element_located(
            (By.ID,"nav-logo")
        )
    )
    print(logo_text)
    assert logo_text.text == ".in"
