import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class JsPopup:
    def popup(self):
        driver = webdriver.Chrome()
        driver.get("http://localhost:5173/handle-alerts")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//button[@id='simple-alert-btn']")
            )
        )
        button.click()
        print(f"Button was clicked")
        print(driver.switch_to.alert.text)
        
        driver.switch_to.alert.accept()

        print(f"Button was accepted")
        time.sleep(5)

JSDemo = JsPopup()
JSDemo.popup()
