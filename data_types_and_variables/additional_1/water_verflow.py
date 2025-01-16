n = int(input())

CAPACITY = 255
total = 0

for i in range(n):
    flow = int(input())
    if total + flow > CAPACITY:
        print("Insufficient capacity!")
    else:
        total += flow

print(total)
