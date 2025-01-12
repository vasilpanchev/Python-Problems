string = input()
capital_indexes = []
for i in range(len(string)):
    if string[i].isupper():
        capital_indexes.append(i)

print(capital_indexes)