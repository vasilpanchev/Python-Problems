from typing import List


def merge(elements: List, start_index: int, end_index: int):
    if start_index < 0:
        start_index = 0
    elif start_index >= len(elements):
        start_index = len(elements) - 1
    if end_index >= len(elements):
        end_index = len(elements) - 1
    merged_list = []
    for i in range(start_index, end_index + 1):
        merged_list.append(elements[i])

    elements[start_index] = ''.join(merged_list)
    new_list = elements[:start_index + 1] + elements[end_index + 1:]
    return new_list


def divide(elements: List, index: int, partitions: int):
    element = elements[index]
    partition_size = len(element) // partitions
    divided = []
    for i in range(0, len(element), partition_size):
        if i == partitions * partition_size - partition_size:
            divided.append(element[i:])
            break
        divided.append(element[i:i + partition_size])
    new_list = elements[:index] + divided + elements[index + 1:]
    return new_list


def main():
    list_of_elements = input().split()
    command = input()
    while True:
        if command == "3:1":
            print(' '.join(list_of_elements))
            break

        action, argument_1, argument_2 = command.split()

        if action == "merge":
            start_index = int(argument_1)
            end_index = int(argument_2)
            list_of_elements = merge(list_of_elements, start_index, end_index)
        elif action == "divide":
            index = int(argument_1)
            partitions = int(argument_2)
            list_of_elements = divide(list_of_elements, index, partitions)

        command = input()


if __name__ == "__main__":
    main()
