numbers = sorted(list(map(int, input().split())), reverse=True)
average = sum(numbers) / len(numbers)
above_average = []
i = 0
while numbers[i] > average and len(above_average) < 5:
    above_average.append(numbers[i])
    i += 1

if len(above_average) == 0:
    print("No")
else:
    print(' '.join([str(num) for num in above_average]))
