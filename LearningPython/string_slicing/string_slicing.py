x = ("text", "button", "deer" ,"tree")
print(x[1:3]) #here string starts from 0 so letters between 1 and 3, including 1 and excluding 3
print(x[2:])
print(x[3:1]) #here output will be empty string as after 3 there is no string

a = [1, 2, 2, 3, 4]
print(a[1:3])
print(a[1:3:2])

y=[2, 4, 6, 8, 10, 12, 14]
print(y[2:6:3]) #first 6 -> as 2nd index then take 3 steps(index 2,3,4) and print 12
print(y[0:6:2])
# first index would be included and will add 2 steps from first index
# then it will include index 2 and will skip 2 indexes and will add 5th index
