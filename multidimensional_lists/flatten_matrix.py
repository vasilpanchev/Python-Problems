from typing import List


def flatten(matrix: List[List]) -> List:
    result = []
    for row in matrix:
        for num in row:
            result.append(num)
    return result


rows = 4
cols = 4
matrix = [[i + 1 for i in range(row * cols, (row + 1) * cols)] for row in range(rows)]
print(flatten(matrix))
