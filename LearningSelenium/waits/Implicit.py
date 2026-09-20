from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ImplicitWait:
    def implicit_wait(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://login.salesforce.com/")
        driver.find_element(By.ID,"username").send_keys("test@ter.com")
wait = ImplicitWait()
wait.implicit_wait()
