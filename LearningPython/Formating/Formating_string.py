a = "hello"
b = "my"
print(a + " " + b + " is Sidharth") # traditional way to format

print("%s %s name is sidharth"%(a,b)) # another way to format string

#format method(recommended)
print("{} {} name is sidharth".format(a,b))
print("{come} {this} name is sidharth".format(come=a,this=b)) 