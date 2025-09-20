budget = float(input())
employees = int(input())
price_per_clothing = float(input())

decoration = budget * 0.1

if employees > 150:
    price_per_clothing *= 0.9  # or price_per_clothing = price_per_clothing * 0.9

total_price = (price_per_clothing * employees) + decoration
needed_money = total_price - budget
leftover_money = budget - total_price

if total_price > budget:
    print(f"Not enough money! \nWingard needs {needed_money:.2f} leva more.")
else:
    print(f"Action! \nWingard starts filming with {leftover_money:.2f} leva left.")