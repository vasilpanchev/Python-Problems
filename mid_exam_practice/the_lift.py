waiting = int(input())
wagons = list(map(int, input().split()))
for i in range(len(wagons)):
    if wagons[i] < 4:
        people_to_add = 4 - wagons[i]
        if waiting >= people_to_add:
            waiting -= people_to_add
            wagons[i] += people_to_add
        else:
            wagons[i] += waiting
            waiting = 0
            break

if waiting == 0 and sum(wagons) != len(wagons) * 4:
    print(f"The lift has empty spots!\n{' '.join([str(wagon) for wagon in wagons])}")
else:
    print(f"There isn't enough space! {waiting} people in a queue!\n{' '.join([str(wagon) for wagon in wagons])}")