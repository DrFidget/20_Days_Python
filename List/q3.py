# 3. Write a program to remove all duplicate elements from a list.
lst = [1, 2, 3, 4, 5, 7, 8, 4, 3, 2, 2, 12, 0, 34]

unique = list(set(lst))  # set have no duplicates

print(unique)
