from typing import List
import random


def add_matrices(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    if not len(matrix1) == len(matrix2) or not len(matrix1[0]) == len(matrix2[0]):
        return []
    sum_matrix = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            sum_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    return sum_matrix


rows = 3
cols = 4
matrix1 = [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows)]
matrix2 = [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows)]
print(matrix1)
print(matrix2)
print(add_matrices(matrix1, matrix2))