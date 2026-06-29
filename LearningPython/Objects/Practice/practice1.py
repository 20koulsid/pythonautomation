# 1 Create a class Triangle
# attributes: base, height
# method: area() → return (1/2) * base * height
import math
from unittest import result


class triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area_calculate(self):
        return (self.height*self.base)/2
area1 = triangle(6,89)
print(area1.area_calculate())
# Create a class Square
# attribute: side
# method: area()
# method: perimeter()
class square:
    def __init__(self,a):
        self.a = a
    def area_calculate(self):
        return(self.a * self.a)
    def perimeter_calucation(self):
        return((self.a)*4)
area2 = square(90)
print(area2.area_calculate())
perimeter = square(89)
print(perimeter.perimeter_calucation())
# Create a class Circle
# attribute: radius
# method: area()
# method: circumference()
class circle:
    def __init__(self,r):
        self.r = r
    def area_calculation(self):
        return(math.pi * self.r**2)
    def circumference_calculation(self):
        return(2 * math.pi * self.r)
area_circle = circle(80)
print(area_circle.area_calculation())
circumference_circle = circle(82)
print(circumference_circle.circumference_calculation())
# 1. Base Page
# Create a class BasePage:
# __init__(driver)
# method open_url(url)
# method get_title()
class BasePage:
    def __init__(self,driver):
        self.driver = driver
        # driver → local variable (comes from outside)
        # self.driver → class-level variable (stored inside the object)
        # So we are saving the driver inside the class instance
    def open_url(self,url):
        return (url)
    def get_title(self):
        return("Google")
page = BasePage("chrome_driver")
result = page.open_url("http://google.com")
print(result)
title = page.get_title()
print(title)
# 2. Login Page
# Create class LoginPage (inherit from BasePage):
# enter_username(username)
# enter_password(password)
# click_login()
class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    def enter_username(self,username):
        print(f"typing username: {username}")
    def enter_password(self,password):
        print(f"typing password: {password}")
    def click_login(self):
        print("Clicking login button")
        return("login successful")
   # alternate method
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return DashboardPage(self.driver)
page = LoginPage("chrome_driver")
result = page.login("user","Admin@123")
print(result)

# 4. Dashboard Page
# Create class DashboardPage:
# get_user_name()
# logout()
class DashboardPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    def get_user_name(self):
        return ("Sid")
    def logout(self):
        print("Logging out")
        return("Logged out successfully")
    # alterna

# 5. Navigation
# Modify login():
# return DashboardPage object
