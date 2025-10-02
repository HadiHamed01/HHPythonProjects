name = input()

best_player_name = ""
best_player_goals = 0

while name != "END":
    goals_scored = int(input())
    if goals_scored > best_player_goals:
        best_player_goals = goals_scored
        best_player_name = name

    if goals_scored >= 10:
        best_player_goals = goals_scored
        best_player_name = name
        break

    name = input()

print(f"{best_player_name} is the best player!")

if goals_scored >= 3:
    print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_player_goals} goals.")