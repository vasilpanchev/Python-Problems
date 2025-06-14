from typing import List


def find_diagonal_elements(matrix: List[List]) -> List[List]:
    if not len(matrix) == len(matrix[0]):
        return [[]]
    main_diagonal = []
    anti_diagonal = []
    for i in range(len(matrix)):
        main_diagonal.append(matrix[i][i])
        anti_diagonal.append(matrix[len(matrix) - i - 1][i])
    result = [main_diagonal, anti_diagonal]
    return result


rows = 3
cols = 3
matrix = [[i + 1 for i in range(row * cols, (row + 1) * cols)] for row in range(rows)]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
print(find_diagonal_elements(matrix))
