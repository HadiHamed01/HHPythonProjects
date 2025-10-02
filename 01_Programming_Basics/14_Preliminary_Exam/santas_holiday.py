room_for_one_person_price = 18.00
apartment_price = 25.00
president_apartment_price = 35.00

days_staying = int(input())
type_of_room = input()
feedback = input()

nights_staying = days_staying - 1
price = 0

if type_of_room == "room for one person":
    price = room_for_one_person_price * nights_staying

elif type_of_room == "apartment":
    price = apartment_price * nights_staying
    if days_staying < 10:
        price *= 0.70
    elif days_staying <= 15:
        price *= 0.65
    elif days_staying > 15:
        price *= 0.50

elif type_of_room == "president apartment":
    price = president_apartment_price * nights_staying
    if days_staying < 10:
        price *= 0.90
    elif days_staying <= 15:
        price *= 0.85
    elif days_staying > 15:
        price *= 0.80

if feedback == "positive":
    price *= 1.25
elif feedback == "negative":
    price *= 0.90

print(f"{price:.2f}")