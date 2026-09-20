import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class DemoWindow:
    def demo_window(self):
        driver = webdriver.Chrome()
        driver.get("https://in.bookmyshow.com/explore/home/hyderabad")
        parent_handle = driver.current_window_handle
        print(f"parent_handle: {parent_handle}")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        print(f"cookie pop up was clicked")

        all_handles = driver.window_handles
        print(f"all_handles: {all_handles}")
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                print(f"user switched to first child handle")
                wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH,"//div[@id='vms_variantOfautocomplete_container']")
                    )
                ).click()
                time.sleep(4)
                driver.close()
                print(f"first child window has been closed successfully")
                time.sleep(4)
                break
        driver.switch_to.window(parent_handle)
        print(f"user has been now switched to parent handle again")
        hotels = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='container responsivegrid']//a[2]")
            )
        )
        hotels.click()
        print(f"hotels option was clicked again")
        time.sleep(4)
indigo_window = DemoWindow()
indigo_window.demo_window()


