while True:
    command = input()
    if command == "End":
        break
    if command == "SoftUni":
        continue
    for letter in command:
        print(letter * 2, end='')
    print()
