# Write a program to merge two sorted lists into a single sorted list.


def merge(lst1, lst2):
    i = 0
    j = 0
    lst = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            lst.append(lst1[i])
            i += 1
        elif lst1[i] > lst2[j]:
            lst.append(lst2[j])
            j += 1

    while i < len(lst1):
        lst.append(lst1[i])
        i += 1
    while j < len(lst2):
        lst.append(lst2[j])
        j += 1

    return lst


list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

merged = merge(list1, list2)
print("Merged Sorted List:", merged)
