from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DemoBrowserCommands:
    def browser_commands(self):
        driver = webdriver.Chrome()

        # Open URL
        driver.get("https://www.amazon.in")

        # Browser information
        print("Current URL:", driver.current_url)
        print("Title:", driver.title)

        # Browser operations
        driver.maximize_window()
        time.sleep(2)

        driver.refresh()
        time.sleep(2)

        # Click on Sell link
        driver.find_element(By.LINK_TEXT, "Sell").click()
        time.sleep(2)

        # Browser navigation
        driver.back()
        time.sleep(2)

        driver.forward()
        time.sleep(2)

        # Close browser
        driver.quit()


demo = DemoBrowserCommands()
demo.browser_commands()