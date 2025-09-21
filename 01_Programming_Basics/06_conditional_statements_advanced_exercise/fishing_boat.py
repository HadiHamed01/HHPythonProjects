budget = int(input())
season = str(input())
fishermen_count = int(input())

boat_price = 0
discount = 0
extra_discount = 0

if season == "Spring":
    boat_price = 3000
elif season == "Summer" or season == "Autumn":
    boat_price = 4200
elif season == "Winter":
    boat_price = 2600

if fishermen_count <= 6:
    discount = 0.10
elif fishermen_count <= 11:
    discount = 0.15
elif fishermen_count >= 12:
    discount = 0.25

if fishermen_count % 2 == 0 and season != "Autumn":
    extra_discount = 0.05

total_discount = (1 - discount) * (1 - extra_discount)
total_price = boat_price * total_discount

if budget >= total_price:
    print(f"Yes! You have {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva.")