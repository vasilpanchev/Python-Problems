from typing import List


def rotate(matrix: List[List]) -> List[List]:
    result = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result[i][len(matrix) - j-1] = matrix[j][i]
    return result


rows = 3
cols = 3
m = [[i + 1 for i in range(row * cols, (row + 1) * cols)] for row in range(rows)]
print(rotate(m))
