import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# if we have any partial link text - half text is static and some part is dynamic
class  DemoFindElementByTagName():
    def locate_by_tag_name(self):
        driver = webdriver.Chrome()
        driver.get("https://www.dazn.com/en-IN/account/content/DAZN/signup?brand=dazn&signin=true&page=emailDetails")
        # driver.find_element(By.TAG_NAME,"input").click()
        driver.find_element(By.CLASS_NAME,"JDqvM").send_keys("saies01@yopmail.com")
findbySelector = DemoFindElementByTagName()
findbySelector.locate_by_tag_name()
time.sleep(500)