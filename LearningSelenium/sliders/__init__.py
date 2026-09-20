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
        driver.get("https://www.amazon.in")
        wait = WebDriverWait(driver, 10)
        search = wait.until(
            EC.presence_of_element_located(
                (By.XPATH,"//input[@id='twotabsearchtextbox']")
            )
        )
        search.click()
        time.sleep(3)
        search.send_keys("tv units")
        search_submit_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH,"//input[@id='nav-search-submit-button']")
            )
        )
        search_submit_button.click()
        slider_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH,"//div[@class='a-section s-range-input-container s-upper-bound']")
            )
        )
        time.sleep(2)
        #ActionChains(driver).drag_and_drop_by_offset(slider_element,30,0).perform()
        # ActionChains(driver).click_and_hold(slider_element).pause(2).move_by_offset(60,0).release().perform()
        ActionChains(driver).move_to_element(slider_element).pause(2).click_and_hold(slider_element).move_by_offset(80,0).release().perform()
        time.sleep(3)
sliders = Sliders()
sliders.new_sliders()
