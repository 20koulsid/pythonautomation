# Beginner Level
# Write a program to divide two numbers and handle division by zero.
try:
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    if num2 == 0:
        raise Exception("Please enter number greater than zero")
    print(num1 / num2)
except Exception as e:
    print(e)
# Write a program that accepts an integer from the user and handles invalid input.
try:
    num = int(input("Please enter a number: "))
    print(f"{num} is an integer")
except ValueError as e:
    print("Error!",e)
finally:
    print("Program is done")
# Create a list of 5 elements. Ask the user for an index and display the element.
# Handle invalid indexes.
try:
    element = ["disk", "deer","cat","dog","fish" ]
    index = int(input("Please enter a number: "))
    print(element[index])
except IndexError as e:
    print("Invalid index, Please enter index from 0 to 4")
except ValueError as e:
    print("Invalid input, Please enter valid integer")
finally:
    print("Program is done")
# Create a dictionary of student names and marks. Ask the user for a name and
# display the marks. Handle missing keys.
try:
    Student = {
        "Shul" : 88,
        "Markus" : 98,
        "Sid" : 90
    }
    user = input("Please enter a name: ")
    print(Student[user])
except KeyError:
    print("Student does not exist")
finally:
    print("Program is done")
# Convert a user-entered string to an integer and handle conversion errors.
try:
    str1 = input("Please enter a string: ")
    print(type(str1))
    str2 = int(str1)
    print(str2)
except ValueError:
    print("Please enter a valid integer")
finally:
    print("Program is done")
# Ask the user to enter two numbers and display their sum. Handle invalid inputs.
try:
    number1 = int(input("Please enter a number: "))
    number2 = int(input("Please enter second number: "))
    print(number1 + number2)
except ValueError:
    print("Please enter a valid integer")
finally:
    print("Program is done")
# Create a list and allow the user to remove an element by index. Handle invalid indexes.
try:
    items = ["tree","sugar","hit","trunk"]
    index = int(input("Please enter index to be removed: "))
    removed_item = items.pop(index)
    print(f"{removed_item} is removed")
    print(f"updated list is {items}")
except IndexError:
    print("Please enter index from 0 to 3")
except ValueError:
    print("Please enter a valid integer")
finally:
    print("Program is done")
# Ask the user to enter a filename and display its contents.
# Handle file-not-found errors.
try:
    file_name = {
        "content1" : "Anime",
        "content2" : "Crime",
        "content3" : "Family",
        "content4" : "Horror",
    }
    fileName = input("Please enter file name: ")
    print(f"file contents: {file_name[fileName]}")
except KeyError:
    print("File does not exist")

try:
    file_name = input("Please enter file name: ")
    with open(file_name) as file:
        print(file.read())
except FileNotFoundError:
    print("File does not exist")

# Write a program that accepts a positive number and raises an exception if the
# number is negative.
try:
    number = int(input("Please enter a number: "))
    if number < 0:
        raise Exception("Negative numbers are not allowed")
except ValueError:
    print("Please enter a valid integer")
except Exception as e:
    print(e)
else:
    print(number)
# Write a program that keeps asking for a valid integer until the user enters one.
while True:
    try:
        integer = int(input("Please enter a number: "))
        if integer == 80:
            print("Correct integer")
        else:
            print("Incorrect integer. Try again")
        break
    except ValueError:
        print("Please enter the integer again")
#Intermediate Level
# Build a calculator that supports addition, subtraction, multiplication,
# and division with proper exception handling.
while True:
    try:
        number3 = float(input("Please enter a number: "))
        number4 = float(input("Please enter a number: "))
        operation = input("Please enter your operation(+,-,*,/): ")
        def add(number3, number4):
            return number3 + number4
        def subtract(number3, number4):
            return number3 - number4
        def multiply(number3, number4):
            return number3 * number4
        def divide(number3, number4):
            if number4 == 0:
                raise ZeroDivisionError("Division by zero not possible")
            return number3 / number4

        if operation == "+":
            print(add(number3, number4))
        elif operation == "-":
            print(subtract(number3, number4))
        elif operation == "*":
            print(multiply(number3, number4))
        elif operation == "/":
            print(divide(number3, number4))
        break
    except ValueError:
        print("Please enter the integer again")
    except ZeroDivisionError as e:
        print(e)

# Create an ATM withdrawal program that prevents withdrawals greater than the available balance.
while True:
    try:
        withdraw_amount = float(input("Please enter your withdrawal amount: "))
        balance = 10000000
        if withdraw_amount > balance:
            print("You cannot withdraw more than your balance")
            continue
        else :
            updated_balance = balance - withdraw_amount
            print(f"You have successfully withdrew {withdraw_amount} amount")
            print(f"Available balance: {updated_balance}")
        break
    except ValueError:
        print("Please enter the withdrawal amount again")
# Write a program to validate a user's age for voting eligibility.
while True:
    try:
        age = int(input("Please enter your age: "))
        if age < 18:
            print("You are not eligible to vote")
            continue
        else:
            print("You are eligible to vote. Please proceed")
        break
    except ValueError:
        print("Please enter the age again")
# Create a password validator that raises an exception if the password
# does not meet specified rules.
while True:
    try:
        password = input("Please enter your password: ")
        if len(password) < 8:
            raise Exception("Password must be at least 8 characters")
        elif not any(char.isupper() for char in password):
            raise Exception("Password must contain at least one uppercase letter")
        elif not any(char.isdigit() for char in password):
            raise Exception("Password must contain at least one number")
        print("Password is valid. User successfully logged in")
        break
    except Exception as e:
        print(e)
# Accept student marks and raise an exception if marks are outside the range 0–100.
while True:
    try:
        marks = float(input("Please enter your marks: "))
        if marks < 0:
            raise Exception("Marks must be positive numbers")
        else:
            print(f"You have scored {marks} marks")
        break
    except ValueError:
        print("Please enter the marks again")
# Write a program to calculate the average of numbers entered by the user and handle
# invalid inputs.
while True:
    try:
        num1 = int(input("Please enter your first number: "))
        num2 = int(input("Please enter your second number: "))
        num3 = int(input("Please enter your third number: "))
        average = ((num1 + num2 + num3) / 3)
        print(f"Average of {num1},{num2},{num3} is {average}")
        break
    except ValueError:
        print("Please enter the valid integers")

while True:
    try:
        products = {
            "trimmer": 1200,
            "shaving kit": 800,
            "shaving cream": 250,
            "shaving bag": 500
        }

        user_input = input("Please enter your product: ")

        print(f"{user_input} is available.")
        print(f"Price: ₹{products[user_input]}")
        break

    except KeyError:
        print("Product not found. Please enter a valid product.")
# Read numbers from a file and calculate their sum while handling file and data errors.
# Create a login system that validates username and password.
# Write a program that repeatedly asks for a valid number until the user enters one.


# Advanced Level
# Create a custom exception called InsufficientBalanceError and use it in a banking application.
# Create a custom exception called InvalidSalaryError and use it to validate employee salaries.
# Create a custom exception called InvalidCredentialsError for a login system.
# Write a shopping cart program that raises exceptions for invalid quantities and out-of-stock products.
# Create a student management system that handles invalid student IDs and missing records.
# Build a library management system with custom exceptions for unavailable books.
# Create an electricity bill calculator that validates user input and unit consumption.
# Build an employee database application that handles invalid employee IDs and salary updates.
# Create a program that validates email addresses and raises exceptions for invalid formats.
# Write a program that validates phone numbers and handles incorrect formats.
# Real-World Practice
# Build a banking system with deposit, withdrawal, balance inquiry, and transaction history.
# Create an expense tracker that stores expenses in a file and handles file-related exceptions.
# Build a hospital management system that validates patient IDs and appointment details.
# Create an online ticket booking system that handles unavailable seats and invalid bookings.
# Build a hotel reservation system with room availability checks and custom exceptions.
# Create a payroll management system that validates employee data and salary calculations.
# Build a food ordering application that handles unavailable menu items and invalid quantities.
# Create a school result management system that validates marks and calculates grades.
# Build an inventory management system that prevents negative stock updates.
# Create a vehicle rental system that validates customer details and vehicle availability.
# Expert Level
# Write a program that logs all exceptions to an errors.txt file.
# Create a nested exception handling program that reads a file, converts data to integers, and performs calculations.
# Write a program that handles ValueError, TypeError, KeyError, IndexError, and ZeroDivisionError in a single application.
# Create your own exception hierarchy for a banking application.
# Build a file backup utility that handles missing files and permission issues.
# Create a multithreaded program and handle exceptions occurring in different threads.
# Build a mini database application using files and handle all possible exceptions.
# Create a REST API client that handles network and response-related exceptions.
# Build a command-line employee management application with complete exception handling.
# Develop a complete banking application using custom exceptions, file handling, logging, and transaction management.