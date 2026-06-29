# 1. Person Class
# Create class Person
# attributes: name, age
# method: display info
from unittest import result


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_info(self):
        print("Name:",self.name)
        print("Age:",self.age)
person1 = Person("Sid",27)
person1.display_info()
# 🔹 2. Car Class (Constructor)
# Create class Car
# brand, model via __init__
class Car_class:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def display_car_info(self):
        print("Brand: ",self.brand)
        print("Model: ",self.model)
car_details = Car_class("BMW","X10")
car_details.display_car_info()
# 🔹 3. Calculator Class
# method: add(a, b) → return result
class calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return (f"The sum of {self.a} and {self.b} is {self.a+self.b}")
sum = calculator(90,444)
print(sum.add())
# 🔹 4. Fix Constructor Error
# class Student:
#     def __init__(name, age):
#         self.name = name
#         self.age = age


# 🔹 5. BankAccount
# deposit()
# withdraw()
# check_balance()
class BankAccount:
    def __init__(self,account_no,amount,account_password):
        self.account_no = account_no
        self.amount = amount
        self.account_password = account_password
    def deposit(self,amount):
        self.amount += amount
        print(f"Please wait while your {amount} is deposited.")
        print(f"{self.amount} deposited successfully on your account.")
    def withdraw(self,amount,password):
        if password != self.account_password:
            print("Incorrect password.")
            return
        if amount > self.amount:
            print("Insufficient fund.")
        elif amount <= 0:
            print("invalid amount withdrawal.")
        else:
            self.amount -= amount
            print(f"{amount} withdrew successfully from your account.")
            print(f"Remaining balance : {self.amount}")
    def check_balance(self):
        print(f"Your account balance is {self.amount}")
acc = BankAccount("4339087782828282",50000,"Admin@password")
acc.deposit(90000)
acc.withdraw(10000,"Admin@password")
# 🔹 6. Counter
# increment()
# decrement()
class Counter:
    def __init__(self,number):
        self.number = number
    def increment(self):
        self.number += 1
        return self.number
    def decrement(self):
        self.number -= 1
        return self.number
number = Counter(23232323232)
print(number.increment())
print(number.decrement())
# 🔹 7. Greeting
# method returns message (not print)
class Greetings:
    def __init__(self,name):
        self.name = name
    def message(self, name):
        return f"Hello {name}!"
msg = Greetings("John")
print(msg.message("John"))
# 🔹 8. Laptop Objects
# create 2 objects
# print details
class Laptop1:
    def __init__(self,model,name,price,manufacture_year):
        self.name = name
        self.price = price
        self.manufacture_year = manufacture_year
        self.model = model
    def display_info(self):
        print("Name:",self.name)
        print("Price:",self.price)
        print("Manufacture Year:",self.manufacture_year)
        print("Model:",self.model)
lap1 = Laptop1("DTE090MNL","Hp","70000","2022")
print(lap1.display_info())
# 🔹 9. Employee Default Value
# salary default = 10000
class Employee_default_value:
    def __init__(self,name,employee_id,email,salary=10000):
        self.name = name
        self.employee_id = employee_id
        self.email = email
        self.salary = salary
    def display_info(self):
        return f"Name: {self.name}, Employee ID: {self.employee_id}, Email: {self.email}, Salary: {self.salary}"
emp1 = Employee_default_value("Harsh",909922,"harsh@cmp.com")
emp2 = Employee_default_value("Prakash",324290888,"prakash@cmp.com")
print(emp1.display_info())
print(emp2.display_info())
# 🔹 10. Login Validation
# validate(user, pwd)
# return Success / Fail
class LoginValidation:
    def __init__(self,email = "sk90@gmail.com",password ="Admin@2000"):
        self.email = email
        self.password = password
    def login(self,user,pwd):
        if user == self.email and pwd == self.password:
            return ("Logged in successfully")
        else:
            return ("Incorrect email or password.")
login_user = LoginValidation()
user_name1 = input("Please enter your username: ")
password1 = input("Please enter your password: ")
result1 = login_user.login(user_name1,password1)
print(result1)
# 🔹 11. ShoppingCart
# add_item()
# remove_item()
# show_items()
class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self,item):
        self.items.append(item)
        print(f"{item} added to your cart.")
    def remove_item(self,item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} removed from your cart.")
        else:
            print("No items in your cart.")
    def showItems(self):
        if self.items:
            print("Items present in your cart.")
            for item in self.items:
                print('-',item)
        else:
            print("Cart is empty.")

cart = ShoppingCart()

cart.add_item("Laptop")
cart.add_item("Mouse")
cart.add_item("keyboard")
cart.add_item("SSD")
cart.showItems()
cart.remove_item("Mouse")
cart.showItems()


# 🔹 12. Company (Class Variable)
# company_name (class variable)
# employee_name (instance variable)
class Company():
    company_name = "ABC PVT Ltd"
    def __init__(self,employee_name):
        self.employee_name = employee_name
    def display_info(self):
        print(f"Company name: {self.company_name}")
        print(f"Employee name: {self.employee_name}")
employee1 = Company("Sirthan")
employee2 = Company("Lonbv")
employee1.display_info()
employee2.display_info()
# 🔹 13. Count Objects
# count how many objects created
class Count():
    count = 0
    def __init__(self):
        Count.count += 1
        print(Count.count)
obj1 = Count()
obj2 = Count()
obj3 = Count()
obj4 = Count()


# 🔹 14. Inheritance
# Animal → speak()
# Dog inherits Animal
class Animal():
    def speak(self):
        print("Animal makes sound")
class Dog(Animal):
    def barks(self):
        print("Dog barks")

    def speak(self):
        print("Dog barks loudly")

dog = Dog()
dog.barks()
dog.speak()
# 🔹 15. Method Override
# override speak() in Dog
def speak(self):
    print("Dog barks loudly")
dog.speak()
# 🔹 16. Private Variable
# make balance private
# access via method
class BankBalance():
    def __init__(self,balance):
        self._balance = balance
        # here _ is used as private variable
    def get_balance(self):
        return self._balance
    def deposit(self,amount):
        self._balance += amount
        print(f"{self._balance} amount has been deposited successfully.")
    def withdraw(self,amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Amount withdrawn.\nBalance left: {self._balance}")
        else:
            print("Insufficient funds")
account = BankBalance(2000000000)
account.withdraw(100000)
account.deposit(39039303939392)
# 🔹 17. Method Calling Method
# call one method inside another

# 🔹 18. Compare Objects
# compare values of 2 objects

# 🔹 19. Static Method
# multiply(a, b)

# 🔹 20. User Class
# login()
# logout()
# is_logged_in

# 🟡 REAL-WORLD MINI PRACTICE
# 🔹 21. EcommerceUser
# login()
# add_to_cart()
# logout()
# maintain cart list
class Login():
    def __init__(self,driver):
        self._driver = driver
    def user_name(self,username):
        print(f"typing the username {username}")
# 🔹 22. Order System
# place_order()
# cancel_order()
# order_history
# 🔹 23. Product Class
# name, price
# apply_discount()
# 🔹 24. Cart Total
# calculate total price of items
# 🔹 25. Full Flow
#
# 👉 Create classes:
#
# User
# Product
# Cart
#
# 👉 Flow:
# login → add product → view cart → logout