# inheritance means inherit some properties from parent
class ParentClass:
    def __init__(self):
        print("parent class inheritence")
    def parent_method(self):
        print("Parent money")

class ChildClass(ParentClass):
    pass

c = ChildClass()
c.parent_method()
# p = ParentClass()
# p.parent_method()

# by using inheritence we can use parent class method in child class

class RateOfInterest:
    # variable below class and accessible to all is class variable
    interest_rate = 6.7
    def __init__(self,name,loan_amount):
        # setting instance variable
        # name and loan are instance variable tied to particular object
        self.name = name
        self.loan_amount = loan_amount
        # self.interest_rate = interest_rate
    def CalculateInterest(self):
        print("the total interest: ",self.loan_amount * self.interest_rate)
class Student(RateOfInterest):
    interest_rate = .03
s = Student("hurtek",5000)
s.CalculateInterest()