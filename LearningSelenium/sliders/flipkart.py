import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Sliders:
    def new_sliders(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.flipkart.com/")
        wait = WebDriverWait(driver, 10)
        close_popup = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@role='button']")
            )
        )
        close_popup.click()
        print(f"Close pop button was clicked")
        search = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Search for Products, Brands and More'])[1]")
            )
        )
        search.click()
        print(f"Search placeholder was selected")
        time.sleep(3)
        search.send_keys("tv units")
        print(f"tv unit text was passed in placeholder")
        search_submit_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@type='submit']")
            )
        )
        search_submit_button.click()
        print(f"submit button was clicked")
        time.sleep(3)
        element1 = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='G12X4V'])[1]")
            )
        )
        element2 = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//div[@class='G12X4V'])[2]")
            )
        )
        # Move the element 1 to right +ve individually

        # ActionChains(driver).drag_and_drop_by_offset(element1),30,0).perform()
        # ActionChains(driver).click_and_hold(slider_element).pause(2).move_by_offset(60,0).release().perform()
        # (ActionChains(driver).move_to_element(element1).pause(2).click_and_hold(element1).move_by_offset
        #  (80, 0).release().perform())

        # Move the element2 to left -x offset

        # ActionChains(driver).drag_and_drop_by_offset(element1,30,0).perform()
        # ActionChains(driver).click_and_hold(slider_element).pause(2).move_by_offset(60,0).release().perform()
        # (ActionChains(driver).move_to_element(element1).pause(2).click_and_hold(element1).move_by_offset
        #  (80, 0).release().perform())

        # In case we want to move both elements
        ActionChains(driver).drag_and_drop_by_offset(element1, 30, 0).perform()
        print(f"Action chain was performed on element1 and slider has been moved to right offest successfully")
        time.sleep(3)
        ActionChains(driver).drag_and_drop_by_offset(element2, -30, 0).perform()
        print(f"Action chain was performed element2 and slider has been moved to left with negative offest successfully")
        # ActionChains(driver).click_and_hold(slider_element).pause(2).move_by_offset(60,0).release().perform()
        # (ActionChains(driver).move_to_element(element1).pause(2).click_and_hold(element1).move_by_offset
        #  (80, 0).release().perform())


        time.sleep(3)


sliders_new = Sliders()
sliders_new.new_sliders()
