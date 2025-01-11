quantity_of_decorations_per_shopping = int(input())
days_left = int(input())
spirit_points = 0
money_spent = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

ornament_set_points = 5
tree_skirt_points = 3
tree_garland_points = 10
tree_lights_points = 17

for day in range(1, days_left + 1):
    # shopping
    if day % 2 == 0:
        spirit_points += ornament_set_points
        money_spent += quantity_of_decorations_per_shopping * ornament_set_price
    if day % 3 == 0:
        spirit_points += tree_skirt_points + tree_garland_points
        money_spent += quantity_of_decorations_per_shopping * (tree_skirt_price + tree_garland_price)
    if day % 5 == 0:
        spirit_points += tree_lights_points
        money_spent += quantity_of_decorations_per_shopping * tree_lights_price
    if day % 15 == 0:
        spirit_points += 30

    # cat
    if day % 10 == 0:
        spirit_points -= 20
        money_spent += tree_skirt_price + tree_garland_price + tree_lights_price
    if day % 11 == 0:
        quantity_of_decorations_per_shopping += 2

if days_left % 10 == 0:
    spirit_points -= 30

print(f"Total cost: {money_spent}")
print(f"Total spirit: {spirit_points}")
