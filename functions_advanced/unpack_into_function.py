def sum_all(*args: int) -> int:
    total = 0
    for num in args:
        total += num
    return total


nums = [1, 5, 3, 0, 19]
print(sum_all(*nums))
