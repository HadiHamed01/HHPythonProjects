orders = int(input())
price = 0
total = 0

for i in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_daily = int(input())

    if not 0.01 <= price_per_capsule <= 100:
        continue
    if not 1 <= days <= 31:
        continue
    if not 1 <= capsules_needed_daily <= 2000:
        continue

    else:
        price = price_per_capsule * capsules_needed_daily * days
        total += price
        print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total:.2f}")