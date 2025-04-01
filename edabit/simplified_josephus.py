n = int(input())
people = [x + 1 for x in range(n)]

current_killer = 0
while len(people) > 1:
    killed = (current_killer + 1) % len(people)
    people.pop(killed)
    current_killer = (current_killer + 1) % len(people) if killed > current_killer else current_killer % len(people)


print(people[0])