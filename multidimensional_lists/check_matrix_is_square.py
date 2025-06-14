from typing import List


def is_square(matrix: List[List]) -> bool:
    return len(matrix) == len(matrix[0])


rows = 3
# cols = 4
cols = 3
matrix = [[i + 1 for i in range(row * cols, (row + 1) * cols)] for row in range(rows)]
print(is_square(matrix))
