from typing import List


def swap(arr: List[int], i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr: List[int]):
    for i in range(len(arr)):
        current = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                swap(arr, i, j)


def sort_cols(matrix: List[List[int]]):
    for i in range(len(matrix[0])):
        current = [0 for _ in range(len(matrix[0]))]
        for j in range(len(matrix)):
            current[j] = matrix[j][i]
        bubble_sort(current)
        for j in range(len(matrix)):
            matrix[j][i] = current[j]


rows = 4
cols = 4
a = [[(rows * cols) - i for i in range(row * cols, (row + 1) * cols)] for row in range(rows)]
for row in a:
    for num in row:
        print(num, end=' ')
    print()
print()
sort_cols(a)
for row in a:
    for num in row:
        print(num, end=' ')
    print()
