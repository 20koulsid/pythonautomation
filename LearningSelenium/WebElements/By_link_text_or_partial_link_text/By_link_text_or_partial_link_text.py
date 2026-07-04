import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# if we have any partial link text - half text is static and some part is dynamic
class  DemoFindElementByLinkText():
    def locate_by_link_text(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.find_element(By.LINK_TEXT,"Yatra for Business").click()
findbySelector = DemoFindElementByLinkText()
findbySelector.locate_by_link_text()
time.sleep(500)
