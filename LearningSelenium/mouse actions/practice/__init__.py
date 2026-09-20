import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
# Q1 — Basic IFrame
# Website: W3Schools IFrame Example
# Write Selenium code to:
# Open the page.
# Find the iframe.
# Switch into it.
# Find an element inside the iframe.
# Print its text.
# Switch back to the main document.
# Concepts: switch_to.frame() / default_content()
# class IFrame():
#     def frame(self):
#         driver = webdriver.Chrome()
#         driver.get("http://localhost:5173/handle-frames")
#         driver.maximize_window()
#         wait = WebDriverWait(driver, 10)
#         frame_element = wait.until(
#             EC.presence_of_element_located(
#                 (By.ID,"simple-frame")
#             )
#         )
#         driver.switch_to.frame(frame_element)
#         print(f"driver switched to frame")
#         button_click = wait.until(
#             EC.presence_of_element_located(
#                 (By.XPATH,"//button[@id='frame-btn']")
#             )
#         )
#         button_click.click()
#         print(f"{button_click.text} was clicked")
#         # if i want to access the main buttons on main page rather than inside frame after
#         # switching to frame we use below
#         driver.switch_to.default_content()
#         print("Switched back to main document")
#         driver.quit()
# new_frame = IFrame()
# new_frame.frame()
# Q2 — IFrame by WebElement
# Website: Selenium Frames Practice
# Write code to:
# Locate an iframe.
# Store it in a variable.
# Switch using the WebElement.
# Interact with an element inside it.
# Return to the parent document.
class NewFrame:
    def new_frame(self):
        driver = webdriver.Chrome()
        driver.get("http://localhost:5173/")
        wait = WebDriverWait(driver, 10)
        frames_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH,"//main[@class='main']//a[1]")
            )
        )
        frames_button.click()
        print(f"frame button was clicked")
        time.sleep(2)
frames_handler = NewFrame()
frames_handler.new_frame()
# Q3 — Nested IFrames 🔥
# Website: Selenium Nested Frames Demo
# Write code to:
# Identify the outer iframe.
# Switch into it.
# Find the nested iframe.
# Switch into the nested iframe.
# Locate an element inside it.
# Print its text.
# Use parent_frame().
# Return to the main document


# 🖱️ Mouse Action
# Q4 — Mouse Hover
# Website: Selenium Actions Demo
# Write code to:
# Locate an element.
# Hover over it using ActionChains.
# Verify the resulting UI change.
# Use:
# ActionChains(driver).move_to_element(element).perform()

# Q5 — Right Click
#
# Website: The Internet — Context Menu
#
# Write Selenium code to:
#
# Locate the box.
# Perform a right click.
# Handle the JavaScript alert.
# Print the alert text.
# Accept the alert.
#
# Use:
#
# actions.context_click(element).perform()
# Q6 — Double Click
#
# Website: The Internet — Add/Remove Elements
#
# This page isn't specifically a double-click demo, so don't force double-click into this exercise. Instead, use it to practice normal ActionChains.click() versus WebElement.click().
#
# Task:
#
# Locate Add Element.
# Click it using .click().
# Add another element using ActionChains.
# Compare the behavior.
# 🟠 Drag & Drop
# Q7 — Drag and Drop ⭐
#
# Website: The Internet — Drag and Drop
#
# Write code to:
#
# Locate box A.
# Locate box B.
# Drag A → B.
# Verify that the positions/text changed.
#
# First try:
#
# actions.drag_and_drop(source, target).perform()
#
# Then try doing it manually with:
#
# click_and_hold()
# move_to_element()
# release()
#
# This is a very good interview exercise.
#
# 🔥 Combined IFrame + Mouse
# Q8 — IFrame + Mouse Hover
#
# Use:
#
# Selenium Frameset Demo
#
# Your task:
#
# Main page
#    ↓
# iframe
#    ↓
# Find element
#    ↓
# Move mouse to element
#    ↓
# Click
#
# Requirements:
#
# switch_to.frame()
# ActionChains
# move_to_element()
# click()
# default_content()
# 🔴 Q9 — IFrame + Right Click
#
# Use:
#
# Selenium Web Interactions Demo
#
# Your task:
#
# Find the iframe if present.
# Switch into it.
# Locate an interactive element.
# Perform context_click().
# Handle whatever UI/alert appears.
# Return to the parent document.
# 🔥🔥 Q10 — Full Challenge
#
# Use Selenium's own test pages:
#
# Selenium Web Test Pages
#
# Create one Python class that demonstrates:
#
# 1. Switch to iframe
# 2. Switch to nested iframe
# 3. parent_frame()
# 4. default_content()
# 5. Mouse hover
# 6. Left click
# 7. Right click
# 8. Double click
# 9. Click and hold
# 10. Drag and drop
# 11. Move by offset
# 12. Keyboard + mouse combination