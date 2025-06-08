line = input()
t = []
while line:
    t.append(int(line))
    line = input()
t = tuple(t)
unique = set(t)
if len(t) == len(unique):
    print("TRUE")
else:
    print("FALSE")
