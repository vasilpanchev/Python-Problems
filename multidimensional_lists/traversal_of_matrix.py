from typing import List


def traversal(matrix: List[List]) -> List[List]:
    traversed = []
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(1, rows + cols):
        col = max(0, i - rows)
        count = min(i, cols - col, rows)
        for j in range(count):
            row_index = min(rows, i) - j - 1
            col_index = col + j
            traversed.append(matrix[row_index][col_index])
    return traversed


matrix = [[11, 42, 25, 51],
          [14, 17, 61, 23],
          [22, 38, 29, 12],
          [27, 81, 29, 71]]
print(traversal(matrix))
