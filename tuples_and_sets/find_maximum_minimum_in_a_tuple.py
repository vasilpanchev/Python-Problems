import sys


def tuple_max(tup: tuple):
    current_max = -sys.maxsize
    for element in tup:
        if element > current_max:
            current_max = element
    return current_max


def tuple_min(tup: tuple):
    current_min = sys.maxsize
    for element in tup:
        if element < current_min:
            current_min = element
    return current_min


numbers = (34, 12, 56, 78, 23)
print(tuple_max(numbers))
print(tuple_min(numbers))
