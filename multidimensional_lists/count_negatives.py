def count_negatives(matrix):
    m, n = len(matrix), len(matrix[0])
    row, col, count = 0, n - 1, 0

    while row < m and col >= 0:
        if matrix[row][col] < 0:
            count += (col + 1)
            row += 1
        else:
            col -= 1
    return count


matrix = [
    [-3, -2, -1, 1],
    [-2, 2, 3, 4],
    [4, 5, 7, 8]
]
print(count_negatives(matrix))
