from typing import List


def is_magic_square(matrix: List[List[int]]) -> bool:
    n = len(matrix)
    if n == 0 or len(matrix[0]) != n:
        return False

    magic_constant = n * (n ** 2 + 1) // 2
    for i in range(n):
        if sum(matrix[i]) != magic_constant:
            return False
        if sum(matrix[j][i] for j in range(n)) != magic_constant:
            return False

    if sum(matrix[i][i] for i in range(n)) != magic_constant:
        return False
    if sum(matrix[i][n - i - 1] for i in range(n)) != magic_constant:
        return False

    return True


magic_square = [
    [7, 8, 0],
    [8, 0, 7],
    [0, 7, 8]
]
print(is_magic_square(magic_square))  # Output: True
