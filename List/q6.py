# 6. Create a function to check if a list is sorted in ascending order.


def checksort(lst):
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            continue
        else:
            return False

    return True


lst = [1, 2, 3, 4, 7]

print(checksort(lst))
