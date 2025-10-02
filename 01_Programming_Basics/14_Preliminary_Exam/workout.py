from math import ceil

days = int(input())
starting_kilometers = float(input())

current_kilometers = starting_kilometers
total_kilometers = 0

for day in range(days):
    percentage_added = int(input())
    current_kilometers += (current_kilometers * (percentage_added / 100))
    total_kilometers += current_kilometers

total_kilometers += starting_kilometers

if total_kilometers >= 1000:
    extra_kilometers = total_kilometers - 1000
    print(f"You've done a great job running {ceil(extra_kilometers)} more kilometers!")
else:
    needed_kilometers = 1000 - total_kilometers
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(needed_kilometers)} more kilometers")