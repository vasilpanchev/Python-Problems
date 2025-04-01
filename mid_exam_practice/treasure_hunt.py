initial_loot = input().split("|")
command = input()
while command != "Yohoho!":
    command = command.split()
    action = command[0]
    if action == "Loot":
        items = command[1:]
        for item in items:
            if item not in initial_loot:
                initial_loot.insert(0, item)
    elif action == "Drop":
        index = int(command[1])
        if index in range(len(initial_loot)):
            removed_loot = initial_loot.pop(index)
            initial_loot.append(removed_loot)
    elif action == "Steal":
        count = int(command[1])
        stolen = []
        if count >= len(initial_loot):
            stolen = [item for item in initial_loot][::-1]
            initial_loot = []
        else:
            while count > 0:
                stolen.append(initial_loot.pop(-1))
        print(', '.join(stolen))
    command = input()

if initial_loot:
    average_gain = sum(len(item) for item in initial_loot) / len(initial_loot)
    print(f"Average treasure gain: {average_gain} pirate credits.")
else:
    print("Failed treasure hunt.")
