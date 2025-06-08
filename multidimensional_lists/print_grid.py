rows = 3
cols = 3
matrix = [[i + 1 for i in range(row * cols, (row + 1) * cols)] for row in range(rows)]

for row in matrix:
    for num in row:
        print(num, end=" ")
    print()
