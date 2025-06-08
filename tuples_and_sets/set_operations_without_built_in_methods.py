def union(set1, set2):
    set1 = list(set1)
    set2 = list(set2)
    union_set = set(set1 + set2)
    return union_set


def intersection(set1, set2):
    set1 = list(set1)
    set2 = list(set2)
    intersected = []
    for item in set1:
        if item in set2:
            intersected.append(item)
    return set(intersected)


def difference(set1, set2):
    set1 = list(set1)
    set2 = list(set2)
    differentiated = []
    for item in set1:
        if item not in set2:
            differentiated.append(item)
    return set(differentiated)


X = {1, 2, 3}
Y = {3, 4, 5}
print(union(X, Y))
print(intersection(X, Y))
print(difference(X, Y))
