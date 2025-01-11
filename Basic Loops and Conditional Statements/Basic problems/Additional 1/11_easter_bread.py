budget = float(input())
flour_price_per_kilo = float(input())
eggs_price_per_pack = 0.75 * flour_price_per_kilo
milk_price_per_liter = 1.25 * flour_price_per_kilo
milk_needed = 0.25 * milk_price_per_liter
colored_eggs = 0
current_bread_count = 0
price_for_one_bread_production = flour_price_per_kilo + eggs_price_per_pack + milk_needed

while budget >= price_for_one_bread_production:
    budget -= price_for_one_bread_production
    current_bread_count += 1
    colored_eggs += 3
    if current_bread_count % 3 == 0:
        colored_eggs -= current_bread_count - 2
else:
    print(
        f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs} " +
        f"eggs and {budget:.2f}BGN left.")
