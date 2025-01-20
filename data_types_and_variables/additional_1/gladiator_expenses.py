lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_expense = 0

for lost_fight in range(1, lost_fights_count + 1):

    if lost_fight % 6 == 0:
        total_expense += sword_price + helmet_price + shield_price
    elif lost_fight % 2 == 0:
        total_expense += helmet_price
    elif lost_fight % 3 == 0:
        total_expense += sword_price

    if lost_fight % 12 == 0:
        total_expense += armor_price

else:
    print(f"Gladiator expenses: {total_expense:.2f} aureus")
