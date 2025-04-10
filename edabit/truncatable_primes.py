def prime(number: int) -> bool:
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def left(number: int) -> bool:
    while number:
        if prime(number) and number != 1 and '0' not in str(number):
            number = str(number)
            number = number[1:]
            if number == "":
                number = 0
            else:
                number = int(number)
        else:
            return False
    return True


def right(number: int) -> bool:
    while number:
        if prime(number) and number != 1 and '0' not in str(number):
            number = str(number)
            number = number[:len(number) - 1]
            if number == "":
                number = 0
            else:
                number = int(number)
        else:
            return False
    return True


def truncatable(number: int) -> str:
    is_left = left(number)
    is_right = right(number)
    if is_left and not is_right:
        return "left"
    elif is_right and not is_left:
        return "right"
    elif is_right and is_left:
        return "both"
    else:
        return "False"


print(truncatable(139))
print(truncatable(103))
print(truncatable(9137))
print(truncatable(5939))
print(truncatable(317))
print(truncatable(5))
