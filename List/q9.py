#  Create a function that returns the intersection of two lists.


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


list1 = [1, 3, 5, 7]
list2 = [2, 3, 6, 8]

print(intersection(list1, list2))
