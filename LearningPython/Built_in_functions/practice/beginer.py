# Q1
# Find max element in a list using max().
from operator import add

list1 = [1,2,3,4,5,6,7,6,6]
print(max(list1))
# Q2
# Find min element in a list using min().
print(min(list1))
# Q3
# Take input using input() and print it.
# print(input("Enter any number"))
# Q4
# Take integer input and print double of it.
# x = int(input("Enter any number:"))
# x = x ** 2
# print(x)
# Q5
# Use sum() to add elements of a list.
x = sum(list1)
print(x)
# Q6
# Sort a list using sorted().
t = sorted(list1)
print(t)
# Q7
# Print reversed list using reversed().
k = reversed(list1)
for item in k:
    print(item)
# Q8
# Convert reversed object into list.
k = reversed(list1)
print(list(k))
# Q9
# Use slice() to get first 3 elements.
l = slice(3)
print(list1[l])
# Q10
# Use slice() to get last 2 elements.
o = slice(7,9)
print(list1[o])
# Q11
# Find max from tuple.
tuple = (1,9,89,90,900,23,4,333)
r = max(tuple)
print(r)
# Q12
# Find min from set.
set = {90,20,30,78,100,899,1000,34,76}
i = min(set)
print(i)
# Q13
# Take two inputs and print their sum.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(sum((a,b,)))
# Q14
# Sort list of strings using sorted().
a = ["Ranchi","Delhi","Jammu","Himachal",]
c = sorted(a)
print(c)
# Q15
# Reverse a string using reversed().
x = reversed(a)
for string in x:
    print(string)
# Q16
# Convert reversed string back to string.
# Q17
# Use sum() on tuple.

# Q18
# Use slice() to get middle element.

# Q19
# Print elements using iter() and next() (first 2 items).

# Q20
# Use next() once on a list iterator.