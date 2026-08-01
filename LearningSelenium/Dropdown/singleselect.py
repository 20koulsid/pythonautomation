import time

from selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.common.by import By


class Dropdown:
    def dropdown_select(self):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/select-menu")
        dropdown = driver.find_element(By.XPATH,"//select[@id='oldSelectMenu']")
        dd = select.Select(dropdown)
        dd.select_by_index(1)
        print("Selected:", dd.first_selected_option.text)
        time.sleep(4)
        dd.select_by_value("1")
        print("Selected:", dd.first_selected_option.text)
        time.sleep(4)
        dd.select_by_visible_text("Blue")
        print("Selected:", dd.first_selected_option.text)
        time.sleep(4)
drop_down = Dropdown()
drop_down.dropdown_select()
