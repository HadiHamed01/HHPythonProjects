food_in_kg = int(input())
food_in_grams = food_in_kg * 1000
current_food = input()

while current_food != "Adopted":
    int_current_food = int(current_food)
    food_in_grams -= int_current_food
    current_food = input()

if food_in_grams >= 0:
    print(f"Food is enough! Leftovers: {food_in_grams} grams.")
else:
    print(f"Food is not enough. You need {abs(food_in_grams)} grams more.")