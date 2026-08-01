import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class MultiselectList:
    def multiselect_list(self):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/select-menu")
        dd_demo = driver.find_element(By.ID,"cars")
        dd_multi = Select(dd_demo)
        dd_multi.select_by_index(1)
        print("Selected:", dd_demo.text)
        dd_multi.select_by_visible_text("Volvo")
        print("Selected:", dd_demo.text)
        dd_multi.select_by_value("volvo")
        print("Selected:", dd_demo.text)
        dd_multi.select_by_index(2)
        print("Selected:", dd_demo.text)
        dd_multi.select_by_visible_text("Saab")
        print("Selected:", dd_demo.text)
        dd_multi.select_by_value("saab")
        print("Selected:", dd_demo.text)
        # deselect the value/index/visible text
        dd_multi.deselect_by_value("saab")
        print("Selected:", dd_demo.text)
demo_multiSelect = MultiselectList()
demo_multiSelect.multiselect_list()
time.sleep(4)