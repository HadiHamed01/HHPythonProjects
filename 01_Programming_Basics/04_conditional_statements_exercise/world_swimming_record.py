world_record_in_seconds = float(input())
distance_in_meters = float(input())
seconds_per_meter = float(input())

METERS_AFTER_RESISTANCE_STARTS = 15
LOST_SECONDS = 12.5

total_seconds = seconds_per_meter * distance_in_meters
added_time = int((distance_in_meters / METERS_AFTER_RESISTANCE_STARTS)) * LOST_SECONDS
sum_seconds_after_added_time = total_seconds + added_time
needed_seconds = sum_seconds_after_added_time - world_record_in_seconds

if sum_seconds_after_added_time < world_record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {sum_seconds_after_added_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {needed_seconds:.2f} seconds slower.")