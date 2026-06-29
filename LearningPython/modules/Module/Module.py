# Create a module named calculator.py with functions:
# add()
# subtract()
# multiply()
# divide()
# Import and use all functions in another file.
import Calculator
from Area import Circle

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
Calculator.add(num1,num2)
Calculator.subtract(num1,num2)
Calculator.multiply(num1,num2)
Calculator.divide(num1,num2)
# Create a module greet.py with a function that prints:
# Welcome to Python
# Import and call it.
import Greet
name = input("Enter your name: ")
Greet.greet(name)
# Create a module containing a function that returns the square of a number.
import Square
num = int(input("Enter a number: "))
Square.square(num)
# Create a module with a function that checks whether a number is even or odd.
import Odd_Even
num = int(input("Enter a number: "))
Odd_Even.check_num(num)
# Create a module with a function that finds the larger of two numbers.
import Larger_num
num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))
Larger_num.larger_num(num1, num2)
# Create a module with a function that calculates the area of:
# Circle
# Rectangle
# Triangle
import Area
shape = input("Enter a shape: ").lower()
if shape == "circle":
    radius = float(input("Enter a radius: "))
    Area.Circle(radius)
elif shape == "rectangle":
    length = float(input("Enter a length: "))
    breath = float(input("Enter a breath: "))
    Area.Rectangle(length, breath)
elif shape == "triangle":
    base = float(input("Enter a base: "))
    height = float(input("Enter a height: "))
    Area.Triangle(base, height)
else:
    print("Invalid Shape")
# Create a module with a function that converts:
# Celsius to Fahrenheit
# Fahrenheit to Celsius
# Create a module that returns the factorial of a number.
# Create a module that returns the sum of all numbers in a list.
# Create a module that counts vowels in a string.
# Intermediate
# Create a package called utilities containing:
# calculator.py
# validator.py
#
# Import functions from both files.
#
# Create a package employees containing:
# add_employee()
# remove_employee()
# display_employee()
# Create a package bank with modules:
# deposit.py
# withdraw.py
# balance.py
# Create a module that reads a text file and displays its contents.
# Create a module that writes user input into a file.
# Create a module that counts:
# words
# lines
# characters
# in a text file.
# Create a module that generates a random password.
# Create a module that generates OTPs using the random module.
# Create a package for a student management system:
# add_student()
# update_student()
# delete_student()
# search_student()
# Create a module that validates:
# Email
# Phone number
# PIN code
# OOP + Modules
# Create a module containing a Calculator class and use it from another file.
# Create a module containing a Student class with:
# name
# age
# marks
#
# Display all details.
#
# Create a module containing an Employee class and calculate annual salary.
# Create a package called shapes containing:
# Circle class
# Rectangle class
# Square class
# Create a BankAccount class with:
# deposit()
# withdraw()
# check_balance()
# Create a Library class that can:
# add books
# issue books
# return books
# Create a module with an Animal base class and:
# Dog subclass
# Cat subclass
# Create a package vehicles with:
# Car class
# Bike class
# Truck class
# Advanced
# Create a package structure for an e-commerce application:
# ecommerce/
#     products/
#     orders/
#     payments/
#     users/
# Create a package for a mini ATM application.
# Build a package that manages:
# Login
# Logout
# Registration
# Create a module that uses exception handling for division by zero.
# Create a module that logs errors to a file.
# Create a package that performs CRUD operations on employee records.
# Create a package that stores data in JSON files.
# Create a package that performs CSV operations:
# Read
# Write
# Update
# Create a reusable configuration module that reads settings from a file.
# Build a simple automation framework structure with:
# framework/
#     pages/
#     tests/
#     utilities/
#     reports/
#     config/
# Create your own module and publish it locally so it can be imported into another project.
# Create a complete package-based project:
# User authentication
# File storage
# Logging
# Exception handling
# OOP
# Multiple modules