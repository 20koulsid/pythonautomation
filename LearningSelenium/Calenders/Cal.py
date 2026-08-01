import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Calenders:
    def calenders(self):
        driver = webdriver.Chrome()
        driver.get("https://www.irctc.co.in")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        alert_dismiss_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//button[normalize-space()='English']")
            )
        )
        alert_dismiss_btn.click()
        from_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//input[@aria-label='Enter From station. Input is Mandatory.']")
            )
        )
# below is handling autosuggestion
        from_btn.click()
        from_btn.send_keys("Jammu")
        time.sleep(2)
        search_result = wait.until(
            EC.visibility_of_all_elements_located(
                (By.XPATH,"//ul[@id='pr_id_1_list']/li")
            )
        )
        for result in search_result:
            print(result.text)
            if "JAMMU TAWI" in result.text:
                result.click()
                time.sleep(2)
                break
        to_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//input[@aria-label='Enter To station. Input is Mandatory.']")
            )
        )
        to_btn.click()
        to_btn.send_keys("Mathura")
        wait.until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, "//ul[@id='pr_id_2_list']/li")
            )
        )
        search_result_to = wait.until(
            EC.visibility_of_all_elements_located(
                (By.XPATH,"//ul[@id='pr_id_2_list']/li")
            )
        )
        for result in search_result_to:
            if "MATHURA JN" in result.text.upper():
                print(result.text)
                print(result.is_displayed())
                print(result.is_enabled())
                result.click()
                time.sleep(2)
                break
        seat_tier_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"(//div[@class='ng-tns-c76-10 ui-dropdown ui-widget ui-state-default ui-corner-all'])[1]")
            )
        )
        seat_tier_btn.click()
        classes_result = wait.until(
            EC.visibility_of_all_elements_located(
                (By.XPATH,"//ul[@role='listbox']//li")
            )
        )
        for result in classes_result:
            print(result.text)
            if "AC First Class" in result.text:
                print(result.text)
                print(result.is_displayed())
                print(result.is_enabled())
                result.click()
                time.sleep(2)
                break
# Calenders
        date_select_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"(//input[@class='ng-tns-c69-9 ui-inputtext ui-widget ui-state-default ui-corner-all ng-star-inserted'])[1]")
            )
        )
        date_select_btn.click()

        travel_date = input("Please enter the travel date: ")

        select_date_result = wait.until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, "//div[contains(@class,'ui-datepicker-calendar-container')]//td/a")
            )
        )

        for date in select_date_result:
            print(date.text)

            if date.text == travel_date:
                print("Date Found:", date.text)
                date.click()
                break
        else:
            print("Date not available")
        seat_category_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"(//div[@class='ng-tns-c76-11 ui-dropdown ui-widget ui-state-default ui-corner-all'])[1]")
            )
        )
        seat_category_btn.click()
        seat_select_result = wait.until(
            EC.visibility_of_all_elements_located(
                (By.XPATH,"//ul[@role='listbox']//li")
            )
        )
        for result in seat_select_result:
            print(result.text)
            if "TATKAL" in result.text:
                print(result.text)
                result.click()
                time.sleep(2)
                break
        booking_continue_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//button[normalize-space()='Search Trains']")
            )
        )
        booking_continue_btn.click()
        time.sleep(7)
CalElement = Calenders()
CalElement.calenders()