import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class calenders:
    def calenders_elements(self):
        driver = webdriver.Chrome()
        driver.get("https://www.makemytrip.com/")
        wait = WebDriverWait(driver, 10)
        # wait.until(
        #     EC.element_to_be_clickable(
        #         (By.XPATH,"//button[normalize-space()='ACCEPT']")
        #     )
        # ).click()
        popup_close = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//span[@class='commonModal__close']")
            )
        )
        popup_close.click()
        hotel_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//a[@class='headerIcons makeFlex hrtlCenter column']")
            )
        )
        hotel_button.click()
        departure_date = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//label[@for='departure']")
            )
        )
        departure_date.click()
        element = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='5']"))
        )
        element.click()
Calenders = calenders()
Calenders.calenders_elements()
