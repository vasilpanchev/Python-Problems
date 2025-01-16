from math import ceil

people = int(input())
capacity = int(input())

print(ceil(people/capacity))

'''
if people < capacity:
    print("All the people fit inside the elevator. Only one course is needed")
else:
    courses = int(people / capacity)
    print(f"{courses} course * {capacity} people")
    if people % capacity != 0:
        left_people = people - courses * capacity
        print(f"+1 course * {left_people} persons")
'''
