def sum_digits(n):
    if n <= 1:
        return n
    digit = n % 10
    n = n // 10
    return digit + sum_digits(n)


print(sum_digits(1234))
