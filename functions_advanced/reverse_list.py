def reverse_list(lst: list):
    if not lst:
        return []
    return [lst[-1]] + reverse_list(lst[:-1])


lst = [1, 2, 3, 4]
print(reverse_list(lst))
print(lst)
