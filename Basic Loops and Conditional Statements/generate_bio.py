line = input()
tags = []
while line:
    tags.append(line.strip())
    line = input()

print(', '.join(tags))
