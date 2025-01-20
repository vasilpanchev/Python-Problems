lines = int(input())

opened = 0
closed = 0
is_nested = False
for _ in range(lines):
    line = input()
    if line == "(":
        if opened > closed:
            is_nested = True
        opened += 1
    elif line == ")":
        closed += 1

if is_nested:
    print("UNBALANCED")
elif opened == closed:
    print("BALANCED")
else:
    print("UNBALANCED")
