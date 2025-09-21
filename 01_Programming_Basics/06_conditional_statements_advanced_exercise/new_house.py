roses_price = 5
dahlias_price = 3.80
tulips_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50

flower_type = str(input())
flower_count = int(input())
budget = int(input())

price = 0
discount = 0

if flower_type == "Roses":
    price = roses_price
    if flower_count > 80:
        discount = 0.10
elif flower_type == "Dahlias":
    price = dahlias_price
    if flower_count > 90:
        discount = 0.15
elif flower_type == "Tulips":
    price = tulips_price
    if flower_count > 80:
        discount = 0.15
elif flower_type == "Narcissus":
    price = narcissus_price
    if flower_count < 120:
        discount = -0.15
elif flower_type == "Gladiolus":
    price = gladiolus_price
    if flower_count < 80:
        discount = -0.20

total_price = flower_count * price * (1 - discount)

if budget >= total_price:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")