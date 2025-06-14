from typing import List


def replace(matrix: List[List[int]], value: int, new: int):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == value:
                matrix[i][j] = new


matrix = [[0, 1, 2],
          [2, 5, 8],
          [0, 2, 2]]
for row in matrix:
    for num in row:
        print(num, end=' ')
    print()
print()
replace(matrix, 2, 3)
for row in matrix:
    for num in row:
        print(num, end=' ')
    print()
