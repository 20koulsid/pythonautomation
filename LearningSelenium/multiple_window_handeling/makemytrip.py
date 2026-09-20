import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class DemoWindow:
    def demo_window(self):
        driver = webdriver.Chrome()
        driver.get("https://www.makemytrip.com/")
        driver.maximize_window()
        parent_handle = driver.current_window_handle
        print(f"parent_handle: {parent_handle}")
        wait = WebDriverWait(driver, 10)
        close_popup = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//span[@class='commonModal__close']")
            )
        )
        close_popup.click()
        print(f"pop up has been dismissed")
        gift_card = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//li[@data-cy='tertiaryRowItem_Gift Cards']"
                          "//div[@class='choosFrom__list--itemDesc makeFlex column flexOne']")
            )
        )
        gift_card.click()
        print(f"Gift card option has been selected")
        all_handles = driver.window_handles
        print(f"all_handles: {all_handles}")
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                print("user switched to first child handle")
                wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH,"(//li[@id='actionItems-0'])[1]")
                    )
                ).click()
                time.sleep(7)
                driver.close()
                time.sleep(3)
                break
        driver.switch_to.window(parent_handle)
        print(f"user switched to parent handle")
        gift_card = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//li[@data-cy='tertiaryRowItem_Gift Cards']"
                           "//div[@class='choosFrom__list--itemDesc makeFlex column flexOne']")
            )
        )
        gift_card.click()
        print(f"Gift card option on first handle has been selected again")
        time.sleep(4)
multi_windows = DemoWindow()
multi_windows.demo_window()