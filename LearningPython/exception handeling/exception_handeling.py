try:
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter another number: "))
    if num2 == 0:
        raise Exception("Please enter a number greater than zero")
    print(num1/num2)
except Exception as e:
    print(e)
else:
    print("In the else block")
finally:
    print("This is always executed")