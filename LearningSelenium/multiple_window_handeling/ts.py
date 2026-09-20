from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TsWindow:
    def demo_window(self):
        driver = webdriver.Chrome()
        driver.get("https://www.adanione.com/domestic-airlines/vistara")
        driver.maximize_window()
        parent_handle = driver.current_window_handle
        print(f"parent_handle: {parent_handle}")
        wait = WebDriverWait(driver, 10)
        dismiss_popup = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//span[@role='presentation']")
            )
        )
        dismiss_popup.click()
        print(f"The dismiss pop was clicked")

window  = TsWindow()
window.demo_window()
