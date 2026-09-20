import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver import ActionChains

class MouseHover:
    def demo_mouse_hover(self):
        driver = webdriver.Chrome()
        driver.get("https://www.amazon.in/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        my_account_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH,"//div[@id='nav-link-accountList']")
            )
        )
        chains_actions = ActionChains(driver)
        chains_actions.move_to_element(my_account_button).perform()
        print(f"chain action is performed by hovering the cursor on account and sign in")
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//div[@id='nav-al-wishlist']//li[3]")
            )
        ).click()
        language_hover = wait.until(
            EC.presence_of_element_located(
                (By.XPATH,"//div[@id='icp-nav-flyout']")
            )
        )

        chains_actions.move_to_element(language_hover).perform()
        print(f"chain action is performed by hovering the cursor on language")
        language = wait.until(
            EC.presence_of_element_located(
                (By.XPATH,"(//div[@id='nav-flyout-icp']//span[contains(@dir,'ltr')])[3]")
            )
        )
        language.click()
        print(f"{language.text} was selected")

        time.sleep(5)
mouse_hover = MouseHover()
mouse_hover.demo_mouse_hover()