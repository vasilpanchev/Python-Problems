A = {1, 2, 3}
B = {2, 3, 4}
C = {3, 4, 5}
mixed = A.intersection(B).union(A.intersection(C)).union(B.intersection(C))
print(mixed)