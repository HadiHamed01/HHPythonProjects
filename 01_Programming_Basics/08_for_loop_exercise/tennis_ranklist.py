from math import floor

number_of_competitions = int(input())
starting_points = int(input())

final_points = starting_points
sum_of_wins = 0

for num in range(number_of_competitions):
    rank = str(input())

    if rank == "W":
        final_points += 2000
        sum_of_wins += 1
    elif rank == "F":
        final_points += 1200
    elif rank == "SF":
        final_points += 720

average_points = (final_points - starting_points) / number_of_competitions
percentage = (sum_of_wins / number_of_competitions) * 100

print(f"Final points: {floor(final_points)}")
print(f"Average points: {floor(average_points)}")
print(f"{percentage:.2f}%")