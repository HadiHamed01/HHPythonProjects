vacation_days = int(input())
type_of_residence = str(input())
feedback = str(input())

vacation_nights = vacation_days - 1
price_per_night = 0

if type_of_residence == "room for one person":
    price_per_night = 18

elif type_of_residence == "apartment":
    price_per_night = 25
    if vacation_nights < 10:
        price_per_night *= 0.7
    elif vacation_nights <= 15:
        price_per_night *= 0.65
    else:
        price_per_night *= 0.5

elif type_of_residence == "president apartment":
    price_per_night = 35
    if vacation_nights < 10:
        price_per_night *= 0.9
    elif vacation_nights <= 15:
        price_per_night *= 0.85
    else:
        price_per_night *= 0.8

total_price = price_per_night * vacation_nights

if feedback == "positive":
    total_price *= 1.25
elif feedback == "negative":
    total_price *= 0.9

print(f"{total_price:.2f}")