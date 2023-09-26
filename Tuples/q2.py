# 2. Create a function to find the index of a specific element in a tuple.


def function(t1, e):
    for i, value in enumerate(t1):
        if value == e:
            return i


t1 = (1, 2, 3, 4, 5)
print(function(t1, 4))
