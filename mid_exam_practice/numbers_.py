numbers = list(map(int, input().split()))
numbers = sorted(numbers, reverse=True)
average = sum(numbers) / len(numbers)

top_numbers = [number for number in numbers if number > average][:5]

if len(top_numbers) == 0:
    print("No")
else:
    print(*top_numbers, sep=' ')
