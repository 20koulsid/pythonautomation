import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class RadioButtons:
    def radio_button(self):
        driver = webdriver.Chrome()
        driver.get("https://demos.jquerymobile.com/1.4.5/checkboxradio-radio/")
        wait = WebDriverWait(driver, 10)

        # 1. First Radio Button
        radio_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='ui-radio']//label[@class='ui-btn ui-corner-all ui-btn-"
                           "inherit ui-btn-icon-left ui-radio-off'][normalize-space()='One']")
            )
        )

        # Save the ELEMENT, not the True/False result
        input1 = driver.find_element(By.XPATH, "//input[@id='radio-choice-0a']")

        print("First radio before click:", input1.is_selected())  # Calls it live
        radio_button.click()
        print("First radio after click:", input1.is_selected())  # Calls it live again

        time.sleep(2)  # Reduced sleep so you don't have to wait as long

        # 2. Second Radio Button
        second_radiobutton = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[@for='radio-choice-0b']")
            )
        )

        # Save the ELEMENT
        input2 = driver.find_element(By.XPATH, "//input[@id='radio-choice-0b']")

        print("\nSecond radio before click:", input2.is_selected())  # Added .is_selected()
        second_radiobutton.click()

        # Check both to prove the first one turned off when the second turned on
        print("Second radio after click:", input2.is_selected())
        print("First radio after clicking second:", input1.is_selected())

        driver.quit()  # Always good practice to close the browser


radiodemo = RadioButtons()
radiodemo.radio_button()
time.sleep(17)