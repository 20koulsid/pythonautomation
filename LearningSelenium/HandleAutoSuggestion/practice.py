import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class practiceAutoSuggestion:
    def autoSuggestion(self):
        driver = webdriver.Chrome()
        driver.get("https://www.makemytrip.com/")
        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[@class='commonModal__close']")
            )
        ).click()
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class,'tp-dt-enhanced"
                           "-floating-cta-wrapper')]//div[contains(@class,'tp-dt-enhanced-floating-cta')"
                           "]//div[3]")
            )
        ).click()
        railway_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//li[@class='menu_Trains']//a[@class='headerIcons makeFlex hrtlCenter column']")
            )
        )
        railway_button.click()
        print(railway_button.is_selected())
        depart_from_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//label[@for='fromCity']")
            )
        )
        depart_from_button.click()
        print(depart_from_button.is_selected())
        depart_from = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH,"//input[@placeholder='From']")
            )
        )
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys("Jammu")
        time.sleep(2)
        search_result1 = driver.find_elements(By.XPATH,"//ul[@role='listbox']/li")
        print(len(search_result1))
        print(search_result1)
        for result in search_result1:
            if "Jammu" in result.text:
                result.click()
                time.sleep(4)
                break
        to_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//label[@for='toCity']")
            )
        )
        to_button.click()
        time.sleep(2)
        to_placeholder = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH,"//input[@placeholder='To']")
            )
        )
        to_placeholder.send_keys("Kolkata")
        time.sleep(4)
        search_results = driver.find_elements(By.XPATH,"//ul[@role='listbox']/li")
        print(len(search_results))
        print(search_results)
        for result in search_results:
            if "Howrah" in result.text:
                result.click()
                time.sleep(4)
                break
depart = practiceAutoSuggestion()
depart.autoSuggestion()
