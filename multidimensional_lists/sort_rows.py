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


def sort_rows(matrix: List[List[int]]):
    for i in range(len(matrix)):
        bubble_sort(matrix[i])


rows = 4
cols = 4
a = [[i for i in range((row + 1) * cols, row * cols, -1)] for row in range(rows)]
for row in a:
    for num in row:
        print(num, end=' ')
    print()
print()
sort_rows(a)
for row in a:
    for num in row:
        print(num, end=' ')
    print()
