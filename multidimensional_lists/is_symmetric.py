from typing import List


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix:
        return []

    # rows = len(matrix)
    # cols = len(matrix[0])

    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed[j][i] = matrix[i][j]

    return transposed


def is_symmetric(matrix: List[List[int]]) -> bool:
    if matrix == transpose(matrix):
        return True
    return False


rows = 3
cols = 3
matrix = [[i + 1 for i in range(row * cols, (row + 1) * cols)] for row in range(rows)]
# matrix = [[1 for i in range(row * cols, (row + 1) * cols)] for row in range(rows)]
print(is_symmetric(matrix))
