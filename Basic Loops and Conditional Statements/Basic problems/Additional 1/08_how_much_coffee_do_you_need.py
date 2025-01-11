coffee_needed = 0

while True:
    command = input()
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffee_needed += 1
    elif command == "coding".upper() or command == "dog".upper() or command == "cat".upper() or command == "movie".upper():
        coffee_needed += 2
    elif command == "END":
        print(coffee_needed)
        break
    else:
        continue

    if coffee_needed > 5:
        print("You need extra sleep")
        break
