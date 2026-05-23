# Beginner Level
# 1. Family Hierarchy
# Create:
# Grandparent → method land()
# Parent → method house()
# Child → method car()
#i want to assign variables directly
class Grandparent:
    name_grandparent = "Sartaj"

    def land_grandparents(self):
        print(f"{self.name_grandparent} owns land")


class Parent(Grandparent):
    name_parents = "Gurtej"

    def house_parents(self):
        print(f"{self.name_parents} owns a house built on {self.name_grandparent}'s land")


class Child(Parent):
    name_child = "Talwar"

    def car_child(self):
        print(f"{self.name_child} owns a car and lives in {self.name_parents}'s house")


grandparent = Grandparent()
grandparent.land_grandparents()

parent = Parent()
parent.house_parents()

child = Child()
child.car_child()

#if i want to pass string in obj assigned
# class Grandparent:
#     name_grandparent = "Sartaj"
#
#     def __init__(self, name):
#         self.name = name
#
#     def land_grandparents(self):
#         print(f"{self.name} inherits land")
#
#
# class Parent(Grandparent):
#     name_parents = "Gurtej"
#
#     def __init__(self, name):
#         super().__init__(name)
#
#     def house_parents(self):
#         print(f"{self.name} inherits house on land of grandparents named {self.name_grandparent}")
#
#
# class Child(Parent):
#     name_child = "Talwar"
#
#     def __init__(self, name):
#         super().__init__(name)
#
#     def car_child(self):
#         print(f"{self.name} inherits car in house built by {self.name_parents} on land of {self.name_grandparent}")
#
#
# grandparent = Grandparent("Aman")
# grandparent.land_grandparents()
#
# parent = Parent("Raj")
# parent.house_parents()
#
# child = Child("Sid")
# child.car_child()
# Create object of Child and access all methods.
#
# 2. Animal Chain
# Create:
# Animal → method eat()
# Dog inherits Animal → method bark()
# Puppy inherits Dog → method weep()
# Call all methods using Puppy.
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} eats")
class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks")
class Puppy(Dog):
    def weep(self):
        print(f"{self.name} weeps")
puppy = Puppy("bunny")
puppy.eat()
puppy.bark()
puppy.weep()
# 3. Student System
# Create:
# Person → attributes name
# Student inherits Person → attributes marks
# Topper inherits Student → method is_topper()
# Check if marks are above 90.
class Person:
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks
    def showInfo_Person(self):
        print(f"{self.name} has attained {self.marks} marks")
class Student(Person):
    def showInfo_student(self):
        print(f"{self.name} has attained {self.marks} marks")
class is_topper(Student):
    def showInfo_topper(self):
        if self.marks > 90:
            print(f"{self.name} is topper and has achieved {self.marks} marks")
        else:
            print(f"{self.name} is not a topper")
student1 = is_topper("JIM", 78)
student1.showInfo_student()
student1.showInfo_topper()
student1.showInfo_Person()

# Intermediate Level
# 4. Vehicle Management
#
# Create:
#
# Vehicle → method start()
# Car inherits Vehicle → method drive()
# SportsCar inherits Car → method turbo()
# 5. Bank Account
#
# Create:
#
# Bank → method bank_name()
# Account inherits Bank → method account_details()
# SavingsAccount inherits Account → method calculate_interest()
# 6. Employee Hierarchy
#
# Create:
#
# Employee → attributes name, salary
# Manager inherits Employee → method bonus()
# HR inherits Manager → method conduct_interview()
# Advanced Level
# 7. Online Shopping System
#
# Create:
#
# User → login details
# Customer inherits User → cart methods
# PremiumCustomer inherits Customer → discount method
# 8. School Result System
#
# Create:
#
# School → school name
# Classroom inherits School → class details
# Student inherits Classroom → result calculation
# 9. Smart Device System
#
# Create:
#
# Device → power_on()
# Mobile inherits Device → call()
# SmartPhone inherits Mobile → internet()
# Challenge Exercise
# 10. Build a Mini Hospital System
#
# Create:
#
# Hospital
# Doctor
# Surgeon
#
# Add:
#
# constructors
# method overriding
# use of super()