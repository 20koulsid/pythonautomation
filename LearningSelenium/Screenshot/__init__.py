import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SsElement:
    def ss_element(self):
        driver = webdriver.Chrome()
        try:
            driver.get("https://www.makemytrip.com/")
            wait = WebDriverWait(driver, 10)

            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[@class='commonModal__close']")
                )
            ).click()

            bot_popup = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "//div[contains(@class,'tp-dt-enhanced-floating-cta-wrapper')]"
                     "//div[contains(@class,'tp-dt-enhanced-floating-cta')]//div[3]")
                )
            )
            bot_popup.click()

            nav_bar = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "(//div[@class='fsw_inner returnPersuasion'])[1]")
                )
            )

            if driver.title == "One Way":
                if not nav_bar.screenshot("./test.png"):
                    print("Element screenshot failed")
                if not driver.save_screenshot("./test_full.png"):
                    print("Full page screenshot failed")
            else:
                print(f"Unexpected title: {driver.title}")

        finally:
            driver.quit()


if __name__ == "__main__":
    ss_capture = SsElement()
    ss_capture.ss_element()