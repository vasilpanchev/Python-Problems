from typing import List


def multiply_by_scalar(matrix: List[List[int]], n) -> List[List[int]]:
    result = [[num * n for num in row] for row in matrix]
    return result


rows = 3
cols = 4
matrix = [[i + 1 for i in range(row * cols, (row + 1) * cols)] for row in range(rows)]
print(multiply_by_scalar(matrix, 3))