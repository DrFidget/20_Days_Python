# 1. Write a Python program to find the sum of all elements in a list.
lst = [1, 2, 3, 4, 5, 7, 8, 4, 3, 2, 2, 12, 0, 34]

s = 0
for i in lst:
    s = s+i

print("sum is :", s)

s = sum(lst)

print("sum is :", s)
