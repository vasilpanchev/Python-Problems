A = (1, 2)
B = ('x', 'y')

cartesian_product = set()

for a in A:
    for b in B:
        cartesian_product.add((a, b))

print(cartesian_product)

from itertools import product

cp = set(product(A, B))
print(cp)
