from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DemoFindElementByTagName():
    def locate_by_tag_name(self):
        driver = webdriver.Chrome()
        driver.get("https://www.amazon.in")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )
        lista = driver.find_elements(By.TAG_NAME, "input")
        print(len(lista))
        for input_element in lista:
            print("ID:", input_element.get_attribute("id"))
            print("Name:", input_element.get_attribute("name"))
            print("Type:", input_element.get_attribute("type"))
            print("Value:", input_element.get_attribute("value"))
            print("Placeholder:", input_element.get_attribute("placeholder"))
        time.sleep(4)
findbyid = DemoFindElementByTagName()
findbyid.locate_by_tag_name()
