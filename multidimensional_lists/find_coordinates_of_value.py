from typing import List


def find_indices_of_value(matrix: List[List], value) -> List[List[int]]:
    return [(i,j) for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j] == value]
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[i])):
    #         if value == matrix[i][j]:
    #             return [[i], [j]]
    #
    # return [[], []]


rows = 3
cols = 3
matrix = [[i + 1 for i in range(row * cols, (row + 1) * cols)] for row in range(rows)]
print(find_indices_of_value(matrix, 3))
