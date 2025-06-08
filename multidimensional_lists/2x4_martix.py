rows = 2
columns = 4

matrix = [[row * columns + column + 1 for column in range(columns)] for row in range(rows)]

print(matrix)
