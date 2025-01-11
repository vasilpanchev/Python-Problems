numer_of_orders = int(input())

total = 0

for _ in range(numer_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    if not 0.01 <= price_per_capsule <= 100 or not 1 <= days <= 31 or not 1 <= capsules_needed_per_day <= 2000:
        continue

    price_for_coffee = price_per_capsule * days * capsules_needed_per_day
    total += price_for_coffee

    print(f"The price for the coffee is: ${price_for_coffee:.2f}")

print(f"Total: ${total:.2f}")
