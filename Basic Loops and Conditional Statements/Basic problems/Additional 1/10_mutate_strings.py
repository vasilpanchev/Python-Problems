# strings must be the same length
string1 = input()
string2 = input()

for i in range(len(string1)):
    if string1[i] == string2[i]:
        continue
    else:
        left_part = string2[:i + 1]
        right_part = string1[i + 1:]
        new_string = left_part + right_part
        print(new_string)
