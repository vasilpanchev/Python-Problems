def is_identity(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j == i and matrix[i][j] != 1:
                return False
            if j != i and matrix[i][j] != 0:
                return False
    return True


matrix = [[0, 1, 0], [0, 1, 0], [0, 0, 1]]
print(is_identity(matrix))
