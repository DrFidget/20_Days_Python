# Write a program to count the occurrences of an element in a tuple.


def function(t1, e):
    occurence = 0
    for x in t1:
        if x == e:
            occurence += 1
    return occurence


t1 = (1, 2, 4, 4, 5)
print(function(t1, 4))
