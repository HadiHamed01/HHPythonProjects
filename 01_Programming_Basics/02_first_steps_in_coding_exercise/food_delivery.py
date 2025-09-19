chicken = 10.35
fish = 12.40
vegetarian = 8.15
delivery = 2.50

necessary_chicken = int(input())
necessary_fish = int(input())
necessary_vegetarian = int(input())

total_sum = (chicken * necessary_chicken) + (fish * necessary_fish) + (vegetarian * necessary_vegetarian)
dessert = total_sum * 0.2
final_sum = total_sum + dessert + delivery

print(final_sum)