import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DemoJs():
    def demo_javascript(self):
        driver = webdriver.Chrome()
        # first we used JS to open the url
        driver.execute_script("window.open('https://www.amazon.in/','_self');")
        print(driver.title)
        time.sleep(5)
        # used JS to find the web element
        element = driver.execute_script("return document.getElementsByTagName('div')[10];")
        # used JS to perform action and return and store it in a variable
        driver.execute_script("arguments[0].click();", element)
        time.sleep(5)
        # driver.get("https://google.com")
demojs = DemoJs()
demojs.demo_javascript()


