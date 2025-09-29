easter_cakes = int(input())

best_chef = ""
best_points = 0

for easter_cake in range(easter_cakes):
    personal_points = 0
    chef_name = input()
    command = input()
    while command != "Stop":
        easter_cake_points = int(command)
        personal_points += easter_cake_points
        command = input()
    print(f"{chef_name} has {personal_points} points.")
    if personal_points > best_points:
        best_points = personal_points
        best_chef = chef_name
        print(f"{chef_name} is the new number 1!")
print(f"{best_chef} won competition with {best_points} points!")