import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver import ActionChains

class DemoRightClick:
    def demo_right_click(self):
        driver = webdriver.Chrome()
        driver.get("https://www.amazon.in/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        side_bar = wait.until(
            EC.presence_of_element_located(
                (By.XPATH,"(//a[@id='nav-hamburger-menu'])[1]")
            )
        )
        side_bar.click()
        Alexa = wait.until(
            EC.presence_of_element_located(
                (By.XPATH,"//section[2]//ul[1]//li[1]//a[1]")
            )
        )
        action_chains = ActionChains(driver)
        action_chains.double_click(Alexa).perform()
        print(f"right click was performed successfully")
        time.sleep(4)
right_click = DemoRightClick()
right_click.demo_right_click()