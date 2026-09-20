# Parent & Child Window (Beginner)
# Website:
# https://the-internet.herokuapp.com/windows
# Task
# Open the website.
# Click "Click Here".
# A new window opens.
# Switch to the new window.
# Print its heading.
# Close the child window.
# Switch back to the parent.
# Print the parent page title.
# Practice concepts
# current_window_handle
# window_handles
# switch_to.window()
# close()
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#
#
# class WindowHandle:
#     def window_handling(self):
#         driver = webdriver.Chrome()
#         parent_handling = driver.current_window_handle
#         print(parent_handling)
#         driver.get("https://the-internet.herokuapp.com/windows")
#         driver.maximize_window()
#         wait = WebDriverWait(driver, 10)
#         Click_btn = wait.until(
#             EC.element_to_be_clickable(
#                 (By.XPATH,"//a[normalize-space()='Click Here']")
#             )
#         )
#         print(Click_btn.text)
#         Click_btn.click()
#         all_handles = driver.window_handles
#         print(all_handles)
#         for handle in all_handles:
#             if handle != parent_handling:
#                 driver.switch_to.window(handle)
#                 wait.until(
#                     EC.presence_of_element_located(
#                         (By.XPATH,"//h3[normalize-space()='New Window']")
#                     )
#                 )
#                 time.sleep(2)
#                 driver.close()
#                 time.sleep(2)
#                 driver.switch_to.window(parent_handling)
#                 time.sleep(2)
#                 break
#         time.sleep(4)
#
# handle_wnd = WindowHandle()
# handle_wnd.window_handling()
# Exercise 2: Multiple Tabs
# Website
# https://demoqa.com/browser-windows
# Task
# Open website.
# Click New Tab.
# Switch to the new tab.
# Print the text.
# Close it.
# Return to parent.
# class SwitchNew:
#     def new_switch(self):
#         driver = webdriver.Chrome()
#         parent_window = driver.current_window_handle
#         driver.get("https://demoqa.com/browser-windows")
#         driver.maximize_window()
#         print(parent_window)
#         wait = WebDriverWait(driver, 10)
#         newtab_btn = wait.until(
#             EC.element_to_be_clickable(
#                 (By.XPATH,"//button[@id='tabButton']")
#             )
#         )
#         print(newtab_btn.text)
#         newtab_btn.click()
#         all_handles = driver.window_handles
#         print(f"Parent handle: {parent_window}")
#         print(f"All handles {all_handles}")
#         for handles in all_handles:
#             print(f"Loop handle: {handles}")
#             if handles != parent_window:
#                 driver.switch_to.window(handles)
#                 print(f"Currently switched to:{driver.current_window_handle}")
#                 print(f"Parent is {parent_window}")
#                 heading = wait.until(
#                     EC.presence_of_element_located(
#                         (By.XPATH, "(//h1[normalize-space()='This is a sample page'])[1]")
#                     )
#                 )
#                 print(heading.text)
#                 print(f"Before close {driver.current_window_handle}")
#                 driver.close()
#                 driver.switch_to.window(parent_window)
#                 break
#             time.sleep(4)
# tab_new = SwitchNew()
# tab_new.new_switch()

# Exercise 3: Multiple Windows
# Same website:
# https://demoqa.com/browser-windows
# Task
# Click New Window.
# Switch.
# Verify heading.
# Close.
# Return.
# class  WindowsMulti:
#     def multi_window(self):
#         driver = webdriver.Chrome()
#         driver.get("https://demoqa.com/browser-windows")
#         driver.maximize_window()
#         parent_handle = driver.current_window_handle
#         print(parent_handle)
#         wait = WebDriverWait(driver, 10)
#         new_window_btn = wait.until(
#             EC.element_to_be_clickable(
#                 (By.XPATH,"//button[@id='windowButton']")
#             )
#         )
#         new_window_btn.click()
#         print(new_window_btn.text)
#         all_handles = driver.window_handles
#         print(all_handles)
#         time.sleep(2)
#         for handles in all_handles:
#             if handles != parent_handle:
#                 driver.switch_to.window(handles)
#                 driver.close()
#                 time.sleep(2)
#                 break
# multi = WindowsMulti()
# multi.multi_window()
# Exercise 4: Open Multiple Windows
# Using DemoQA.
# Task
# Click
# New Tab
# New Window
# New Window Message
# Now you'll have four windows.
# Practice:
# Print every window handle.
# Switch to each.
# Print title.
# Close every child.
# Return to parent.
# class MultipleWindows:
#
#     def window_multi(self):
#
#         driver = webdriver.Chrome()
#         driver.get("https://demoqa.com/browser-windows")
#
#         parent_handle = driver.current_window_handle
#
#         print(f"1st/Parent window: {parent_handle}")
#
#         driver.maximize_window()
#
#         wait = WebDriverWait(driver, 10)
#
#         # ==========================================
#         # 1st CTA - New Window
#         # ==========================================
#
#         new_window_btn = wait.until(
#             EC.element_to_be_clickable(
#                 (By.XPATH, "//button[@id='windowButton']")
#             )
#         )
#
#         new_window_btn.click()
#
#         print(f"New window button clicked: {new_window_btn.text}")
#
#         all_handles = driver.window_handles
#
#         print("Handles:", all_handles)
#
#         child_handle1 = all_handles[1]
#
#         print(f"2nd window: {child_handle1}")
#
#         driver.switch_to.window(child_handle1)
#
#         heading = wait.until(
#             EC.visibility_of_element_located(
#                 (By.ID, "sampleHeading")
#             )
#         )
#
#         if heading.text == "This is a sample page":
#             print(f"Heading verified successfully: {heading.text}")
#         else:
#             print("Heading verification failed")
#             driver.save_screenshot(".//test.png")
#
#         driver.close()
#
#         driver.switch_to.window(parent_handle)
#
#         # ==========================================
#         # 2nd CTA - New Tab
#         # ==========================================
#
#         new_tab_btn = wait.until(
#             EC.element_to_be_clickable(
#                 (By.XPATH, "//button[@id='tabButton']")
#             )
#         )
#
#         new_tab_btn.click()
#
#         print(f"New tab button clicked: {new_tab_btn.text}")
#
#         all_handles = driver.window_handles
#
#         print("Handles:", all_handles)
#
#         # Only parent + current child exist
#         child_handle2 = all_handles[1]
#
#         print(f"3rd window: {child_handle2}")
#
#         driver.switch_to.window(child_handle2)
#
#         heading = wait.until(
#             EC.visibility_of_element_located(
#                 (By.ID, "sampleHeading")
#             )
#         )
#
#         if heading.text == "This is a sample page":
#             print(f"Heading verified successfully: {heading.text}")
#         else:
#             print("Heading verification failed")
#             driver.save_screenshot(".//test.png")
#
#         driver.close()
#
#         driver.switch_to.window(parent_handle)
#
#         # ==========================================
#         # 3rd CTA - New Window Message
#         # ==========================================
#
#         message_btn = wait.until(
#             EC.element_to_be_clickable(
#                 (By.XPATH, "//button[@id='messageWindowButton']")
#             )
#         )
#
#         message_btn.click()
#
#         print(f"Message window button clicked: {message_btn.text}")
#
#         time.sleep(2)
#
#         all_handles = driver.window_handles
#
#         print("Handles:", all_handles)
#
#         # Check how many Selenium actually sees
#         print(f"Number of windows: {len(all_handles)}")
#
#         for handle in all_handles:
#
#             if handle != parent_handle:
#
#                 driver.switch_to.window(handle)
#
#                 print(f"Current window: {handle}")
#                 print(f"Title: {driver.title}")
#
#                 body_text = wait.until(
#                     EC.visibility_of_element_located(
#                         (
#                             By.XPATH,
#                             "//body[contains(., 'Knowledge increases by sharing but not by saving')]"
#                         )
#                     )
#                 )
#
#                 if "Knowledge increases by sharing but not by saving" in body_text.text:
#                     print("Text paragraph verified successfully")
#                 else:
#                     print("Text verification failed")
#
#                 driver.close()
#
#                 driver.switch_to.window(parent_handle)
#
#                 break
#
#         driver.quit()
#
#
# windows = MultipleWindows()
# windows.window_multi()

# Exercise 5: Switch by Title
# Instead of using handle order,
# Loop through windows.
# If
# driver.title == "Sample"
# perform actions.
# This is commonly asked in interviews.
class Switch:
    def switch_window(self):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/browser-windows")
        driver.maximize_window()
        parent_window = driver.current_window_handle
        print(parent_window)
        wait = WebDriverWait(driver, 10)
        new_tab_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,"//button[@id='tabButton']")
            )
        )
        new_tab_btn.click()
        wait.until(EC.number_of_windows_to_be(2))
        all_handles = driver.window_handles
        child_handles = all_handles[1]
        print(child_handles)
        heading = wait.until(
            EC.visibility_of_element_located(
                (By.ID,"sampleHeading")
            )
        )
        print(heading.text)
        for child_handles in all_handles:
            driver.switch_to.window(child_handles)
            if driver.title == "sample":
                print(f"You land on correct page with title {driver.title}")
                time.sleep(2)
                driver.close()
                break
        driver.switch_to.window(parent_window)
        time.sleep(4)
window = Switch()
window.switch_window()

# Exercise 6: Switch by URL
# Loop through windows.
# If
# driver.current_url
# contains
# sample
# perform actions.
# Exercise 7: Close Only Child Windows
# Suppose there are 5 windows.
# Write logic to close every child.
# Parent should remain open.
# Exercise 8: Close All Windows
# Loop through
#
# driver.window_handles
#
# Close every window.
#
# Exercise 9: Print All Window Titles
#
# Output example:
#
# Parent Window
# Amazon
#
# Child Window
# Today's Deals
#
# Child Window
# Electronics
# Exercise 10: Amazon Practice
#
# Open
#
# https://www.amazon.in
#
# Click
#
# Today's Deals
#
# If it opens in another tab,
#
# Switch,
#
# Print title,
#
# Close,
#
# Return.
#
# Exercise 11: Flipkart
#
# Open Flipkart.
#
# Click any promotional banner.
#
# Handle new tab.
#
# Verify title.
#
# Return.
#
# Exercise 12: MakeMyTrip
#
# Exactly like your current project.
#
# Tasks:
#
# Close popup.
# Click Trains.
# Handle child window.
# Click offer.
# Close child.
# Return to parent.
# Continue automation.
# Exercise 13: Open Windows Using JavaScript
#
# Instead of clicking,
#
# Create new windows.
#
# driver.execute_script("window.open('https://google.com')")
#
# Practice switching.
#
# Exercise 14: Multiple URLs
#
# Open
#
# Google
#
# Amazon
#
# YouTube
#
# using JavaScript.
#
# Now
#
# Loop through
#
# Print
#
# driver.title
#
# Close all except Google.
#
# Exercise 15: Handle Unknown Number of Windows
#
# Don't assume only one child exists.
#
# Loop through
#
# driver.window_handles
#
# Print
#
# Title
# URL
# Handle
# Exercise 16: Selenium Interview Exercise ⭐
#
# Open
#
# https://demoqa.com/browser-windows
#
# Requirements:
#
# Store parent handle
# Open three windows
# Print all handles
# Switch one by one
# Print title
# Print URL
# Close child
# Switch back
# Verify parent title
# Exercise 17: Verify Window Count
#
# Example:
#
# assert len(driver.window_handles) == 2
#
# or
#
# print(len(driver.window_handles))
# Exercise 18: Dynamic Window Handling
#
# Write a reusable function:
#
# def switch_to_new_window(driver):
#
# It should
#
# get handles
# identify child
# switch
# return child handle
#
# Very useful in frameworks.
#
# Exercise 19: Screenshot Child Window
#
# After switching
#
# Take screenshot
#
# driver.save_screenshot("child.png")
# Exercise 20: Real Framework Practice ⭐⭐⭐
#
# Create functions
#
# open_child_window()
#
# switch_to_child()
#
# perform_actions()
#
# close_child()
#
# switch_parent()
#
# Call them from a test case.
#
# This is how Selenium Page Object Model (POM) frameworks are often structured.
#
# Recommended order
# Parent & Child Window
# New Tab
# New Window
# Switch by Title
# Switch by URL
# Close Child
# Close All
# Multiple Child Windows
# JavaScript Windows
# MakeMyTrip Project