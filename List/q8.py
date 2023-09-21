# 8. Implement a function to find the frequency of a given element in a list.
lst = [1, 2, 3, 4, 8, 8, 8, 7]


def freq(lst, element):
    return lst.count(element)


print(freq(lst, 8))
