from typing import List


def sum_of_rows(l: List[List]) -> List[int]:
    sums = []
    current_row_sum = 0
    for row in l:
        for num in row:
            current_row_sum += num
        sums.append(current_row_sum)
        current_row_sum = 0
    return sums


rows = 3
cols = 3
matrix = [[i + 1 for i in range(row * cols, (row + 1) * cols)] for row in range(rows)]
print(matrix)
print(sum_of_rows(matrix))
