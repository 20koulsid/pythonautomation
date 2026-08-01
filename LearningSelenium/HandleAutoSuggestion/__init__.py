import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AutoSuggestion:
    def autoSuggestion(self):
        driver = webdriver.Chrome()
        driver.get("https://www.makemytrip.com/")
        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//span[@class='commonModal__close']")
            )
        ).click()
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//div[contains(@class,'tp-dt-enhanced"
                         "-floating-cta-wrapper')]//div[contains(@class,'tp-dt-enhanced-floating-cta')"
                          "]//div[3]")
            )
        ).click()
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//label[@for='fromCity']")
            )
        ).click()
        depart_from = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='From']")
            )
        )
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys("New Delhi")
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)
dd_suggestion = AutoSuggestion()
dd_suggestion.autoSuggestion()
