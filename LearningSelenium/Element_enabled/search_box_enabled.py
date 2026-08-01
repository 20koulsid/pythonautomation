import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ElementEnabled:
    def element_enabled(self):
        driver = webdriver.Chrome()
        driver.get("https://www.amazon.in")
        wait = WebDriverWait(driver, 10)

        search_box = wait.until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        print(search_box.is_enabled())
        time.sleep(10)
element_enabled = ElementEnabled()
element_enabled.element_enabled()

