from typing import List
import numpy as np


def determinant(matrix: List[List]) -> float:
    matrix = np.array(matrix)
    result = np.linalg.det(matrix)
    return result


rows = 5
cols = 5
matrix = [[31, 56, 98],
          [12, 53, 23],
          [45, 82, 11]]
print(determinant(matrix))
