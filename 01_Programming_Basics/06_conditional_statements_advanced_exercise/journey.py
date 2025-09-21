budget = float(input())
season = str(input())

price = 0
resort = ""
destination = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.30
        resort = "Camp"
    elif season == "winter":
        price = budget * 0.70
        resort = "Hotel"

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.40
        resort = "Camp"
    elif season == "winter":
        price = budget * 0.80
        resort = "Hotel"

elif budget > 1000:
    destination = "Europe"
    price = budget * 0.90
    resort = "Hotel"

print(f"Somewhere in {destination}")
print(f"{resort} - {price:.2f}")