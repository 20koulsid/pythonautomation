# Positional args
# Required args
def sum(a,b):
    return a+b
c = sum(1,2)
# here 1 -> a, 2 -> b these are positional agrs
# Also if we try to not assign any value it will return error so the value are required
# Keyword agrs
def multiply(u=8 ,j=9):
    return u*j
e = multiply(u =0,j = 88)
# optional args
def sub(a = 1,b = 2):
    return a-b
s = sub(3,4)
# here we already assigned a and b by default so the 2nd value will be optional
# and we can put empty ()

# def factorial(n):
#     if i == 1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(100))

def largest_number(num1,num2,num3):
    if num3 < num1 > num2:
        return num1
    elif num3 < num2 > num1:
        return num2
    elif num1 < num3 > num2:
        return num3

print(largest_number(10,20,30))
print(largest_number(1222,-222,789))
def convert_temp(far):
    # (farhenh * 9/5) + 32 = celcius
    celcius = (far -32) * (1.8)
    return celcius
temp = float(input("Enter a temperature in Fahrenheit: "))
print(f"{convert_temp(temp):.2f} degrees Fahrenheit")