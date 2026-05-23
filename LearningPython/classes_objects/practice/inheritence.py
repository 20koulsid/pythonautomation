# Create a parent class Parent with method show_parent().
import math
from turtle import Shape


class Parent:
    def __init__(self):
        print("parent class inheritence")
    def show_parent(self):
        print("parent class inheritence")
class Child(Parent):
    pass
obj = Child()
obj.show_parent()
# Child class Child should inherit and call it.
class Parent:
    def __init__(self):
        print("parent class inheritence")
    def show_parent(self):
        print("parent class inheritence")
class Child(Parent):
    pass
obj = Child()
obj.show_parent()
# Add method show_child() in Child and call both methods.

# Create Person(name) and child Student. Print name using child object.
class Person:
    def __init__(self,name):
        self.name = name
    def show_info(self):
        print(self.name)
class Student(Person):
    pass
person1 = Student("sid")
person1.show_info()
# Create Person(name, age) and child Employee(name, age, salary). Display all.
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        # We used super() here because it calls the parent class constructor to
        # initialize name and age, so the child class can use those attributes.
        self.salary = salary
    def show_info(self):
        print(f"{self.name}, age {self.age}, earns {self.salary}")
employee1 = Employee("Sid",27,50000)
employee1.show_info()

# Create Animal with eat() and child Dog with bark().
class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"{self.name} eats food")
class Dog(Animal):
    def bark(self):
        print(f"{self.name} bark")

dog = Dog("tommy")
dog.eat()
dog.bark()
# Create Vehicle with method start(). Child Car with method drive().
class Vehicle:
    def Start(self):
        print("Vehicle start")
class Car(Vehicle):
    def drive(self):
        print("Car is driving")
car = Car()
car.Start()
car.drive()
# Create class Company with class variable
# company_name and instance variable employee_name.
class Company:
    company_name = "TYFG Pvt"
    def __init__(self,employee_name):
        self.employee_name = employee_name
    def show_info(self):
        print(f"company name is {self.company_name} \nemployee name is {self.employee_name}")
info = Company("suresh")
info.show_info()
# Create class Bank with interest_rate = 5. Child HDFC overrides it.
class Bank:
    interest_rate = 5
    def __init__(self,customer_name,loan_amount):
        self.customer_name = customer_name
        self.loan_amount = loan_amount
    def CalculateInterest(self):
        print("the total interest is: ", self.loan_amount*self.interest_rate)
class Student(Bank):
    interest_rate = 4
p = Student("Samantha",20000)
p.CalculateInterest()
# Create class with class variable rate = 5 and inside constructor self.rate = 10. Print both.
class Interest:
    rate = 5
    def __init__(self):
        self.rate = 10
    def show_rate(self):
        print(self.rate)
        print(Interest.rate)
user = Interest()
user.show_rate()
# Create Product(name, price) and child Mobile(name, price, brand).
class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
class Mobile(Product):
    def __init__(self,name,price,brand):
        super().__init__(name,price)
        self.brand = brand
    def show_info(self):
        print(f"brand is {self.brand} \nname is {self.name} \nprice is {self.price}")
product = Mobile("SamsungS34",34000,"Samsung")
product.show_info()
# Create Student(name, marks) with method check_pass().
# Create child class Topper with method is_topper().
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def check_pass(self):
        if self.marks > 35:
            print(f"{self.name} has passed")
        else:
            print(f"{self.name} has failed")
class Topper(Student):
    def is_topper(self):
        if self.marks > 98:
            print(f"{self.name} is topper")
        else:
            print(f"{self.name} is not topper")
student = Student("Sam",10)
student.check_pass()
topper = Topper("Sam",90)
topper.is_topper()

# Create Account(name, balance) with method show_balance().
class Account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def show_balance(self):
        print(f"{self.name} balance is {self.balance}")
balance = Account("Sam",109000)
balance.show_balance()
# Create SavingsAccount with method add_interest().
class SavingsAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def add_interest(self):
        if self.balance > 20000:
            self.balance += 2000
            print(self.balance)
        else:
            print(self.balance)
balance = SavingsAccount("Sam",100000)
balance.add_interest()

# Create Shape with method area() and child Rectangle overriding it.
class shape:
    def __init__(self,side1,side2):
        self.side1 = side1
        self.side2 = side2
    def Area(self):
        area = self.side1 * self.side2
        print(area)
class Rectangle(shape):
    def __init__(self,side1,side2):
        super().__init__(side1,side2)
    def Area(self):
        area = self.side1 * self.side2
        print(area)
class Circle(shape):
    def __init__(self,radius):
        super().__init__(radius,radius)
        self.radius = radius
    def circle_area(self):
        area = 3.14 * self.radius * self.radius
        print(area)
circle = Circle(11)
circle.circle_area()
area = Rectangle(1,2)
area.Area()
# 🔹 Intermediate Level
# Create Employee with method work(). Child Developer with method code().
class Employee:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def work(self):
        print(f"{self.first_name} {self.last_name} work at PTC")
class Developer(Employee):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
    def code(self):
        print(f"{self.first_name} {self.last_name} is coder")
code = Developer("saransh","dubey",18)
code.code()
code.work()
# Create Appliance with method power_on(). Child WashingMachine with wash().
class Appliances:
    def __init__(self,name):
        self.name = name
    def power_on(self):
        print(f"{self.name} is on")
class WashingMachine(Appliances):
    def __init__(self,name):
        super().__init__(name)
    def wash(self):
        print(f"{self.name} is washing")
appliance = WashingMachine("top load washing machine")
appliance.power_on()
appliance.wash()
# Create Book(title, author) and child Ebook(title, author, size).
class Book:
    def __init__(self,title,author):
            self.title = title
            self.author = author
    def show_info(self):
        print(f"Book {self.title} written by {self.author}")
class Ebook(Book):
    def __init__(self,title,author):
        super().__init__(title,author)
    def showInfo(self):
        print(f"Ebook {self.title} written by {self.author}")
book = Ebook("Death","Sadhguru")
book.showInfo()
book.show_info()
# Create User(email, password) and child Admin with delete_user().
class User:
    def __init__(self,email,password):
        self.email = email
        self.password = password
    def Login(self):
        print(f"{self.email} is logged in")
class Admin(User):
    def __init__(self,email,password):
        super().__init__(email,password)
    def delete_user(self):
        print(f"{self.email} user deletion is on process")
        print(f"{self.email} is deleted successfully")
user = Admin("k@t.com","Admin@123")
user.Login()
user.delete_user()
# Note in python
# Class names → PascalCase
# Methods → lowercase_with_underscore

# Create Cart with add_item(). Child DiscountCart with apply_discount().
class Cart:
    def __init__(self,name):
        self.name = name
    def add_item(self):
        print(f"{self.name} is added to cart")
class Discount(Cart):
    def __init__(self,name,amount,discount):
        super().__init__(name)
        self.amount = amount
        self.discount = discount
    def apply_discount(self):
        self.amount -= self.discount
        print(f"Discount of {self.discount} is applied to cart ")
        print(f"Final amount is {self.amount}")
cart = Discount("cart",2000,300)
cart.apply_discount()
# Create Teacher(name, subject) and child MathTeacher with method teach_math().
class Teacher:
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject
    def show_subject(self):
        print(f"{self.name} teaches {self.subject}")
class MathTeacher(Teacher):
    def __init__(self,name,subject):
        super().__init__(name,subject)
    def teach_math(self):
        print(f"{self.name} is teacher for {self.subject}")
teacher = MathTeacher("sunita","math")
teacher.teach_math()
teacher.show_subject()
# Create Hospital with method open(). Child Clinic with method treat_patient().
class Hospital:
    def __init__(self,name,address):
        self.name = name
        self.address = address
    def Open(self):
        print(f"{self.name} located near {self.address} is open now")
class ChildClinic(Hospital):
    def __init__(self,name,address):
        super().__init__(name,address)
    def treat_patient(self):
        print(f"{self.name} located at {self.address} is child clinic also.")
patient = ChildClinic("Apollo","durgam cheuvu")
patient.Open()
patient.treat_patient()

# Create Food with method eat(). Child Fruit with method vitamins().
class Food:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"{self.name} has been eaten")
class Fruit(Food):
    def __init__(self,name):
        super().__init__(name)
    def Vitamins(self):
        print(f"{self.name} fruit has 80% vitamins")
food = Fruit("Banana")
food.eat()
food.Vitamins()
# Create Shape with method draw(). Child Circle and Square both override it.
# Create Account with method deposit(). Child CurrentAccount with withdraw().
# Create Account with method deposit(). Child CurrentAccount with withdraw().

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited to account {self.account_number}")
        print(f"Current balance: {self.balance}")

class CurrentAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn from account {self.account_number}")
        else:
            print("Insufficient balance")
        print(f"Current balance: {self.balance}")

# Object creation
acc = CurrentAccount(34629090292828, 300000)

acc.deposit(90000)
acc.withdraw(50000)
# 🔹 Advanced Level
# Create multi-level inheritance:
# Grandparent → method land()
# Parent → method house()
# Child → method car()
class Grandparent:
    def __init__(self,name):
        self.name = name
    def Land(self):
        print(f"{self.name} has 40 acres land ")
class Parent(Grandparent):
    def __init__(self,name):
        super().__init__(name)
    def house(self):
        print(f"{self.name} has home on that 40 acers land ")
class Child(Parent):
    def __init__(self,name):
        super().__init__(name)
    def Car(self):
        print(f"{self.name} has a car inside the parent's house on grandparent land ")
grandparent = Grandparent("surtej")
grandparent.Land()
parent = Parent("gurtej")
parent.house()
child = Child("naamtej")
child.Car()
# Create class Bank with class variable interest_rate. Create two child classes with
# different rates and compare outputs.
# Create class Bank with class variable interest_rate.
# Create two child classes with different rates and compare outputs.

class Bank:
    interest_rate = 0.5

    def __init__(self, name, loan_amount):
        self.name = name
        self.loan_amount = loan_amount

    def CalculateInterest(self):
        interest = self.loan_amount * self.interest_rate
        total = self.loan_amount + interest

        print(f"{self.name} Bank")
        print(f"Loan Amount: {self.loan_amount}")
        print(f"Interest Rate: {self.interest_rate}")
        print(f"Total Amount after Interest: {total}\n")


class Bank1(Bank):
    interest_rate = 0.5


class Bank2(Bank):
    interest_rate = 0.1


# Objects
b1 = Bank1("HDFC", 10000)
b2 = Bank2("SBI", 10000)

# Compare outputs
b1.CalculateInterest()
b2.CalculateInterest()

# Create class Student with class variable school_name. Override it in child class
# CollegeStudent.
class Student:
    school_name = "LOPA School of Public"

    def __init__(self, name, Class, roll_number):
        self.name = name
        self.Class = Class
        self.roll_number = roll_number

    def show_student(self):
        print(f"{self.name} is student of {self.school_name} "
              f"having Roll number {self.roll_number} in class {self.Class}")


class CollegeStudent(Student):
    # Overriding class variable
    school_name = "ABC College"

    def __init__(self, name, Class, roll_number):
        super().__init__(name, Class, roll_number)

    def show_student(self):
        print(f"{self.name} is student of {self.school_name} "
              f"having Roll number {self.roll_number} in class {self.Class}")


# Object of parent class
s1 = Student("Rahul", 10, 25)
s1.show_student()

# Object of child class
s2 = CollegeStudent("Aman", "BCA", 101)
s2.show_student()
# Create method overriding example where child changes behavior of parent method completely.
# Create a real-world system:
# Parent: Order(item, price)
# Child: OnlineOrder(item, price, delivery_charge)
# Add method to calculate final price.