number_of_strings = int(input())

for _ in range(number_of_strings):
    line = input()
    if line.__contains__(',') or line.__contains__('.') or line.__contains__('_'):
        print(f"{line} is not pure!")
    else:
        print(f"{line} is pure.")
