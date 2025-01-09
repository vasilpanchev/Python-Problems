budget = int(input())
spent = 0
command = input()

while command != "End":
    price = int(command)
    spent += price
    if spent > budget:
        print("You went in overdraft!")
        break
    command = input()
else:
    print("You bought everything needed.")
