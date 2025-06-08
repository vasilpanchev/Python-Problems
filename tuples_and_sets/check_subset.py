set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
for element in set1:
    if element not in set2:
        print("False")
        break
else:
    print("True")
