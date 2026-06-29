# # Beginner Level
# # 1. Import Math Module
# # Import the math module
# # Print:
# # square root of 64
# # value of pi
# # factorial of 5
# import math
#
# from MyModule.Student import Average
#
# print(f"square root of 64 is : {(math.sqrt(64))} ")
# print(f"value of pi is : {math.pi} ")
# print(f"value of factorial 5 is : {math.factorial(5)} ")
# # 2. Random Number Generator
# # Use random module
# # Generate:
# # random integer between 1–50
# # random choice from a list
# import random
# number = random.randint(1,50)
# print(number)
# list = ["lopes","sides","guttes"]
# item = random.choice(list)
# print(item)
# # 3. Create Your First Module
# # Create a module named greet.py
# # Add a function to greet a user
# # Import it into another file and call the function
# from MyModule import greet
# name = input("Please enter your name: ")
# greet.greet(name)
# # 4. Import Specific Function
# # Import only one function from math
# # Use it to calculate square root
# from math import sqrt
# print(sqrt(10))
# # 5. Use Alias Name
# # Import a module using alias
# # Print any value or function using alias
# from MyModule import alias
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# alias.multiply(a,b)
# # Easy Intermediate Level
# # 6. Calculator Module
# # Create a module with functions:
# # addition
# # subtraction
# # multiplication
# # division
# # Import and use all functions.
# from MyModule import claculator
# s = int(input("Enter first number: "))
# t = int(input("Enter second number: "))
# claculator.add(s,t)
# claculator.subtract(s,t)
# claculator.divide(s,t)
# claculator.multiply(s,t)
# #
# 7. Student Module
# Create a module that:
# stores student details
# displays marks
# calculates average
from random import choice

from MyModule import Student
# from MyModule.Area import Circle
# from MyModule.Student import Average
#
# name = str(input("Please enter your name: "))
# age = int(input("Please enter your age: "))
# m1 = int(input("Please enter your marks for subject1: "))
# m2 = int(input("Please enter your marks for subject2: "))
# m3 = int(input("Please enter your marks for subject3: "))
# student = Average(name,age,m1,m2,m3)
# student.display()
# student.average()
# 8. Area Calculator Module
# Create functions for:
# area of circle
# rectangle
# square
# triangle
from MyModule.Area import Circle,Rectangle,Triangle,Square
choice = input("Enter shape: ").lower()
if choice == "circle":
    radius = float(input("Enter radius: "))
    shape = Circle(radius)
elif choice == "rectangle":
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    shape = Rectangle(width,height)
elif choice == "square":
    side = float(input("Enter side: "))
    shape = Square(side)
elif choice == "triangle":
    base = float(input("Enter side: "))
    height = float(input("Enter height: "))
    shape = Triangle(base,height)
else:
    print("Invalid shape")
    exit()
shape.area()


# 9. Temperature Converter
# Create module functions for:
# Celsius → Fahrenheit
# Fahrenheit → Celsius
from MyModule import Temperature
temp = float(input("Please enter temperature: "))
print(Temperature.celsius_to_fahrenheit(temp))
print(Temperature.fahrenheit_to_celsius(temp))
# 10. Password Generator
# Using modules:
# generate random password
# password should contain letters and numbers
# Intermediate Level
# 11. Bank Module
#
# Create functions:
#
# deposit
# withdraw
# check balance
# 12. Shopping Cart Module
#
# Create functions:
#
# add item
# remove item
# calculate total bill
# 13. Utility Module
#
# Create functions:
#
# even or odd
# prime number
# palindrome
# Armstrong number
# 14. Datetime Module Practice
#
# Perform tasks:
#
# print current date
# print current time
# calculate age from birth year
# 15. Marksheet Module
#
# Create functions:
#
# total marks
# percentage
# grade calculation
# Advanced Level
# 16. Create a Package
#
# Create package structure with:
#
# student.py
# teacher.py
# __init__.py
#
# Import package into another file.
#
# 17. OS Module Practice
#
# Perform:
#
# create folder
# rename file
# delete file
# list files in folder
# 18. SYS Module Practice
#
# Print:
#
# Python version
# system path
# command-line arguments
# 19. File Handling Module
#
# Create module functions:
#
# write into file
# read file
# append data
# count words
# 20. Library Management Module
#
# Create features:
#
# add book
# search book
# issue book
# return book
# Advanced Challenge Level
# 21. Authentication Module
#
# Create:
#
# user registration
# login validation
# password checking
# 22. Logging Module
#
# Create a module that:
#
# stores logs into file
# records login time
# records errors
# 23. API Helper Module
#
# Create reusable functions for:
#
# GET request
# POST request
# handling API response
# 24. Automation Utility Module
#
# Create functions:
#
# launch browser
# take screenshot
# close browser
# wait for element
# 25. Build Complete Package
#
# Create package structure:
#
# browser module
# login module
# utility module
# report module