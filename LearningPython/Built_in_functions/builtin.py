# max() -> returns largest item
# min() -> returns smallest item in an iterable
# iter() -> returns an iterator object
# reversed() -> returns a reversed iterator
# next() -> returns a next item in an iterator
# slice() -> returns a slice object
# sorted() -> returns a sorted list
# sum() -> Sums the items of an iterator
# input() -> Allows user to enter the value

demo_tuple = (1,34,87,90,89,9)
v = sorted(demo_tuple)
print(v)

k = slice(1,3,2)
print(demo_tuple[k])


i = iter (demo_tuple)
j = reversed(demo_tuple)
print(next(j))
print(next(j))
print(next(j))
# iter is most important method used in automation as we will iter the value one by one
print(next(i))
print(next(i))

print(max(demo_tuple))
print(min(demo_tuple))

