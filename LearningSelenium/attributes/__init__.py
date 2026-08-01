from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DemoGetAttributes:
    def demo_getvalue(self):
        driver = webdriver.Chrome()

        # Open URL
        driver.get("https://www.amazon.in")
# <input type="text" id="email" name="email" placeholder="Enter Email">
# here
# Attribute - type, id, placeholder,
# value - text, email, Enter Email
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")

        print(search_box.get_attribute("id"))
        print(search_box.get_attribute("type"))
        print(search_box.get_attribute("name"))
        print(search_box.get_attribute("placeholder"))
        time.sleep(10)
demo = DemoGetAttributes()
demo.demo_getvalue()
# ❌ Common mistakes
# If you write: driver.find_element(By.CSS_SELECTOR, "twotabsearchtextbox") it will fail.
# Why?
# Because CSS interprets twotabsearchtextbox as a tag name, not an ID.
