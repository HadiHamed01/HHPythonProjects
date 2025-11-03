days = int(input())
number_of_players = int(input())
group_energy = float(input())
water_per_day_per_person = float(input())
food_per_day_per_person = float(input())
current_energy = group_energy
current_water = days * number_of_players * water_per_day_per_person
current_food = days * number_of_players * food_per_day_per_person

for day in range(1, days + 1):
    energy_lost = float(input())
    current_energy -= energy_lost

    if current_energy <= 0:
        print(f"You will run out of energy. You will be left with {current_food:.2f} food and {current_water:.2f} water.")
        break

    if day % 2 == 0:
        current_energy = current_energy * 1.05
        current_water = current_water * 0.70

    if day % 3 == 0:
        food_needed = current_food / number_of_players
        current_food -= food_needed
        current_energy = current_energy * 1.10

if current_energy > 0:
    print(f"You are ready for the quest. You will be left with - {current_energy:.2f} energy!")