sequence_string = input()
sequence_list = sequence_string.split(', ')

if sequence_list[len(sequence_list) - 1] == 'wolf':
    print("Please go away and stop eating my sheep")
else:
    for i in range(len(sequence_list)):
        if sequence_list[i] == "wolf":
            print(f"Oi! Sheep number {len(sequence_list) - i - 1}! You are about to be eaten by a wolf!")
