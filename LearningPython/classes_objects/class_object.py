# Class is example employee -> all details filled is class -> it is blueprint
# object is name
class Employee:
    def __init__(self,first_name,last_name,email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")
user1 = Employee("sarthak","muhrcn","murc.re@t.com")
user1.greet_user()
