from typing import List


def sum_of_2d_list(l: List[List]):
    total_sum = 0
    for row in l:
        for num in row:
            total_sum += num
    return total_sum


rows = 3
cols = 3
matrix = [[i + 1 for i in range(row * cols, (row + 1) * cols)] for row in range(rows)]

print(sum_of_2d_list(matrix))
