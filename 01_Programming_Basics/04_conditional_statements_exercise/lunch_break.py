from math import ceil

series_name = str(input())
episode_length = int(input())
lunch_break_length = int(input())

lunch_time = lunch_break_length * 0.125
relax_time = lunch_break_length * 0.25

total_time = lunch_time + relax_time + episode_length
leftover_time = ceil(lunch_break_length - total_time)
needed_time = ceil(total_time - lunch_break_length)

if lunch_break_length >= total_time:
    print(f"You have enough time to watch {series_name} and left with {leftover_time} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {needed_time} more minutes.")