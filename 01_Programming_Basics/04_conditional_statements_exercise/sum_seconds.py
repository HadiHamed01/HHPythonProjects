from math import floor

time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third
minutes = total_time // 60  # or minutes = int(total_time / 60)
seconds = total_time % 60

minutes = floor(minutes)   # not necessary

if seconds < 10:
    print(f"{minutes}:0{seconds}")   # or print(f"{minutes}:{seconds:02d}")
                                     # because :0.2d will make the one-digit number a two-digit number
else:
    print(f"{minutes}:{seconds}")