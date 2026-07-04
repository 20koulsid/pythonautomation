from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DemoBrowserCommands:
    def browser_commands(self):
        driver = webdriver.Chrome()

        # Open URL
        driver.get("https://www.amazon.in")


demo = DemoBrowserCommands()
demo.browser_commands()