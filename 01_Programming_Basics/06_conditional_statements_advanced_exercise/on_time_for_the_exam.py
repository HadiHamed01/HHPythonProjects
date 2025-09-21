exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time_as_minutes = exam_hour * 60 + exam_minutes
# this is used to transfer the given hours into minutes and add them with the given minutes
arrival_time_as_minutes = arrival_hour * 60 + arrival_minutes

difference = arrival_time_as_minutes - exam_time_as_minutes

if difference > 0:  # arrival_time_as_minutes > exam_time_as_minutes
    print("Late")
    if difference < 60:
        print(f"{difference} minutes after the start")
    else:
        hh = abs(difference) // 60
        mm = abs(difference) % 60
        print(f"{hh}:{mm:02d} hours after the start")

elif difference >= -30:
    print("On time")
    if not difference == 0:
        print(f"{abs(difference)} minutes before the start")

else:
    print("Early")
    if difference > -60:
        print(f"{abs(difference)} minutes before the start")
    else:
        hh = abs(difference) // 60
        mm = abs(difference) % 60
        print(f"{hh}:{mm:02d} hours before the start")