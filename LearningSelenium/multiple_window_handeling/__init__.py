import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MultipleWindows:
    def multiple_windows(self):
        driver = webdriver.Chrome()
        driver.get("https://www.makemytrip.com")
        driver.maximize_window()
        parent_handle = driver.current_window_handle
        print(parent_handle)
        wait = WebDriverWait(driver, 10)
        first_popup_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[@class='commonModal__close']")
            )
        )
        first_popup_btn.click()
        train_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//li[@class='menu_Trains']//a[@class='headerIcons makeFlex hrtlCenter column']")
            )
        )
        train_btn.click()
        all_handles = driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                offer_btn = wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "(//div[@class='slick-slide slick-active slick-current']//div[1]//div[1]//div[1]//div[2]//div[1]//a[1]")
                    )
                )
                offer_btn.click()
                driver.close()
                time.sleep(2)
                break
        # driver.switch_to.window(parent_handle)
        # train_btn.click()
        time.sleep(4)
        # bot_close_btn = wait.until(
        #     EC.element_to_be_clickable(
        #         (By.XPATH, "//div[contains(@class,'tp-dt-enhanced"
        #                    "-floating-cta-wrapper')]//div[contains(@class,'tp-dt-enhanced-floating-cta')"
        #                    "]//div[3]")
        #     )
        # )
        # bot_close_btn.click()
Multi_windows = MultipleWindows()
Multi_windows.multiple_windows()