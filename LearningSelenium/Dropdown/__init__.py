import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select  # 1. Import the Select class


class Dropdown:
    def dropdown_element(self):
        driver = webdriver.Chrome()
        driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
        wait = WebDriverWait(driver, 10)

        # 2. Target the <select> tag, not the <p> tag
        select_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//select")
            )
        )

        # 3. Pass the web element into the Select class
        dropdown = Select(select_element)

        # 4. Choose your option (3 different ways you can do it)

        # Option A: Select by the exact text you see on the screen
        dropdown.select_by_visible_text("India")
        time.sleep(2)

        # # Option B: Select by the underlying HTML 'value' attribute
        # dropdown.select_by_value("ATA")  # Selects Antarctica
        # time.sleep(2)

        # Option C: Select by its index number (0 is the first item)
        dropdown.select_by_index(5)  # Selects Andorra
        time.sleep(5)

        driver.quit()


dropdemo = Dropdown()
dropdemo.dropdown_element()