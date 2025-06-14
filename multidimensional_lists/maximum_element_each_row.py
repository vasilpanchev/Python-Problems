import sys
from typing import List


def maximum_element_each_row(matrix: List[List]):
    maxes = []
    for row in matrix:
        current_max = -sys.maxsize
        for num in row:
            if num > current_max:
                current_max = num
        maxes.append(current_max)
    return maxes


rows = 3
cols = 3
matrix = [[i + 1 for i in range(row * cols, (row + 1) * cols)] for row in range(rows)]
print(maximum_element_each_row(matrix))
