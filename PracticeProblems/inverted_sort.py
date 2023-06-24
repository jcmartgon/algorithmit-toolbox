# Jesus Carlos Martinez Gonzalez
# 15/06/2023
# Inverted Sort

# Write a function called inverted_sort. inverted_ should
# take as input a list of integers, and return as output a
# list with the integers sorted from HIGHEST to LOWEST.
#
# You may use any sorting algorithm you want: bubble, merge,
# insertion, selection, a new sort that you learned on your
# own, or even one you created yourself. You may use loops,
# or you may use recursion.
#
# You may not use Python's native list sort or reverse
# methods; you must write your own sort.


def inverted_sort(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = inverted_sort(lst[0:mid])
    right = inverted_sort(lst[mid:])

    return inverted_merge(left, right)


def inverted_merge(a, b):
    inverted = []
    while len(a) > 0 and len(b) > 0:
        if a[0] >= b[0]:
            inverted.append(a[0])
            del a[0]
        else:
            inverted.append(b[0])
            del b[0]
    inverted += a + b
    return inverted


# The code below will test your function. Feel free to
# modify it. As written originally, it will print the list:
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(inverted_sort([5, 4, 10, 1, 7, 2, 3, 6, 8, 9]))
