import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class  DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/social/common/yatra/signin.html")
        driver.find_element(By.XPATH,"//input[@id='email']").send_keys("test@test.com")
findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()
time.sleep(500)

# class DemoFindElementID():
#     def locate_by_id_demo(self):
#         driver = webdriver.Chrome()
#         driver.get("https://www.dazn.com/en-IN/account/content/dazn/signup?signin=true&page=emailDetails")
#         wait = WebDriverWait(driver, 30)
#         email = wait.until(
#             EC.visibility_of_element_located((By.XPATH, "//input[@id='email']"))
#         )
#         email.send_keys("saies01@yopmail.com")
# findbyid = DemoFindElementID()
# findbyid.locate_by_id_demo()
time.sleep(500)