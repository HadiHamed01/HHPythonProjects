name = str(input())
points_from_academy = float(input())
number_of_judges = int(input())

total_points = points_from_academy

for numbers in range(number_of_judges):
    grader_name = str(input())
    points_from_judge = float(input())

    total_points += (len(grader_name) * points_from_judge) / 2

    if total_points > 1250.5:
        break

if total_points > 1250.5:
    print(f"Congratulations, {name} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {name} you need {1250.5 - total_points:.1f} more!")