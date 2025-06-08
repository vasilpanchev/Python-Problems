data = (1, 3, 2, 3, 4, 2, 3)
data_set = set(data)
highest_count = 0
highest_count_element = None
for element in data_set:
    count = data.count(element)
    if count > highest_count:
        highest_count_element = element
        highest_count = data.count(element)
print(highest_count_element)
print(highest_count)
