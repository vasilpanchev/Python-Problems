number = int(input())
numbers = list(str(number))
'''
size = len(numbers)
largest = []
current_largest = -1
for _ in range(size):
    for j in range(len(numbers)):
        if int(numbers[j]) > int(current_largest):
            current_largest = numbers[j]
    largest.append(current_largest)
    numbers.remove(current_largest)
    current_largest = -1
    
    for digit in largest:
    print(digit, end='')
'''
numbers.sort(reverse=True)
for digit in numbers:
    print(digit, end='')

