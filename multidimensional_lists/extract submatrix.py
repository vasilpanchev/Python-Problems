def extract(matrix, row, col):
    rows = len(matrix) - row
    cols = len(matrix[0]) - col
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(row, len(matrix)):
        for j in range(col, len(matrix[0])):
            result[i - row][j - col] = matrix[i][j]

    return result


rows = 4
cols = 4
row = 2
col = 2
matrix = [[i + 1 for i in range(r * cols, (r + 1) * cols)] for r in range(rows)]
print(matrix)
print(extract(matrix, row, col))
