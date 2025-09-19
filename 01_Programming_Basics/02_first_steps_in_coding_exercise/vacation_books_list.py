pages = int(input())
pages_read_per_hour = int(input())
days = int(input())

sum_of_hours = pages / pages_read_per_hour
hours_per_day = sum_of_hours / days

print (int(hours_per_day))