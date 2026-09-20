from selenium import webdriver
from selenium.common import ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Sliders:
    def new_sliders(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.amazon.in")
        wait = WebDriverWait(driver, 10,2, ignored_exceptions=[ElementNotInteractableException])
        search = wait.until(
            EC.presence_of_element_located(
                (By.XPATH,"//input[@id='twotabsearchtextbox']")
            )
        )
        search.click()

sliders = Sliders()
sliders.new_sliders()