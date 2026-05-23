# Example there is a bank which charges rate of interest same to all customers
# here
class RateOfInterest:
    # variable below class and accessible to all is class variable
    interest_rate = 0.34
    def __init__(self,name,loan_amount):
        # setting instance variable
        # name and loan are instance variable tied to particular object
        self.name = name
        self.loan_amount = loan_amount
        # self.interest_rate = interest_rate
    def CalculateInterest(self):
        print("the total interest: ",self.loan_amount * self.interest_rate)
person1 = RateOfInterest("Karthik",2000000)
# person1.CalculateInterest()
person1.interest_rate = 6.7
person1.CalculateInterest()
person2 = RateOfInterest("hrthik",223000)
person2.CalculateInterest()
person2.interest_rate = 1.7
person2.CalculateInterest()
# Note if we use RateOfIntrest.interest rate instead self.interest rate it will not change
# the value that was assigned later