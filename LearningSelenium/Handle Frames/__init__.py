import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class IFrame:
    def demo_frame(self):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10)
        driver.get("https://www.tutorialspoint.com/selenium/practice/nestedframes.php?utm_source=chatgpt.com")
        driver.maximize_window()
        driver.maximize_window()
        # used id directly
        driver.switch_to.frame("frame1")
        print(f"driver switched to first iframe")
        button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,"header[class='header selenium bg-white p-3 '] div:nth-child(1)")
            )
        )
        button.click()
        print(f"Button Pressed")

        time.sleep(5)
myframe = IFrame()
myframe.demo_frame()