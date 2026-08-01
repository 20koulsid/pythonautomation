from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LearningSelenium.HandleAutoSuggestion.practice import a

class Verify_Checkbox:
    def checkbox(self):
        driver = webdriver.Chrome()
        driver.get("https://www.qa-practice.com/elements/checkbox/mult_checkbox")
        wait = WebDriverWait(driver, 10)
        checkbox_element = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//input[@id='id_checkboxes_0']")
            )
        )
        print("Displayed:", checkbox_element.is_displayed())
        print("Enabled:", checkbox_element.is_enabled())
        checkbox_element.click()
checkbox = Verify_Checkbox()
checkbox.checkbox()