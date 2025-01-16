year = int(input())

unique = set(str(year))

while True:
    year += 1
    unique = set(str(year))
    if len(unique) == len(str(year)):
        print(year)
        break
