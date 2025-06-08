t = ('a', 'b', 'a', 'c', 'b')
unique = set(t)
result = []
for element in t:
    if element in unique:
        result.append(element)
        unique.remove(element)
print(tuple(result))
