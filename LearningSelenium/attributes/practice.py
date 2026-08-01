from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")

wait = WebDriverWait(driver, 10)

logo = wait.until(
    EC.presence_of_element_located((By.ID, "nav-logo-sprites"))
)

print("ID:", logo.get_attribute("id"))
print("Class:", logo.get_attribute("class"))

time.sleep(10)
driver.quit()