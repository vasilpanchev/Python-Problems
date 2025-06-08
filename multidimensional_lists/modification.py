rows = 3
cols = 3
matrix = [[i+1 for i in range(row*cols, (row+1)*cols)] for row in range(rows)]

print(matrix)
print(matrix[1][2])
matrix[0][1] = 10
print(matrix)
