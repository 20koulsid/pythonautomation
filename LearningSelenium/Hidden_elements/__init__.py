import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HiddenElements:

    def element_hidden(self):
        driver = webdriver.Chrome()
        driver.get("https://www.makemytrip.com/hotels")

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

        # Open Rooms & Guests
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class,'roomGuests')]")
            )
        ).click()

        # Click '+' button (example locator)
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@aria-label='Increase value from 0']")
            )
        ).click()

        # Check age dropdown visibility
        element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class,'rmsGst__slctAge--cont')]")
            )
        )

        print("Displayed:", element.is_displayed())

        time.sleep(10)
        driver.quit()

obj = HiddenElements()
obj.element_hidden()