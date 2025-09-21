month = str(input())
nights_count = int(input())

studio_price_per_night = 0
apartment_price_per_night = 0

if month == "May" or month == "October":
    studio_price_per_night = 50
    apartment_price_per_night = 65
    if 14 >= nights_count > 7:
        studio_price_per_night *= 0.95
    elif nights_count > 14:
        studio_price_per_night *= 0.70

elif month == "June" or month == "September":
    studio_price_per_night = 75.20
    apartment_price_per_night = 68.70
    if nights_count > 14:
        studio_price_per_night *= 0.80

elif month == "July" or month == "August":
    studio_price_per_night = 76
    apartment_price_per_night = 77

if nights_count > 14:
    apartment_price_per_night *= 0.90

apartment_total_price = apartment_price_per_night * nights_count
studio_total_price = studio_price_per_night * nights_count

print(f"Apartment: {apartment_total_price:.2f} lv.")
print(f"Studio: {studio_total_price:.2f} lv.")