length = int(input())
width = int(input())
height = int(input())
percent_used = float(input())

total_area_in_cm = length * width * height  #  this is cm^3
total_area_in_litres = total_area_in_cm / 1000  #  or total_area_in_cm * 0.001 because its cm^3
used_area = percent_used / 100
total_litres = total_area_in_litres * (1 - used_area)

print(total_litres)