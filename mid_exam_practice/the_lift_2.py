waiting = int(input())
wagons = list(map(int, input().split()))
for i in range(len(wagons)):
    if waiting > 3:
        people_to_add = 4 - wagons[i]
        waiting -= people_to_add
        wagons[i] += people_to_add
    else:
        wagons[i] += waiting
        waiting = 0

if waiting > 0:
    print(f"There isn't enough space! {waiting} people in a queue!")

elif sum(wagons) != len(wagons) * 4:
    print(f"The lift has empty spots!")

print(f"{' '.join(str(wagon) for wagon in wagons)}")
