import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
signin_Button = driver.find_element(By.CSS_SELECTOR,"#nav-link-accountList > a")
signin_Button.click()
email = driver.find_element(By.ID,"ap_email_login")
email.send_keys("koulsidharth83@gmail.com")
submit_email = driver.find_element(By.CSS_SELECTOR,"#continue > span > input")
submit_email.click()
password  = driver.find_element(By.ID,"ap_password")
password.send_keys("jh")

time.sleep(30)