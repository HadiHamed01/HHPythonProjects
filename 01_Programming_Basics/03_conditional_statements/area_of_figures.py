from math import pi

type_of_shape = input()
area = 0

if type_of_shape == "square":
    side = float(input())
    area = side * side
elif type_of_shape == "rectangle":
    first_side = float(input())
    second_side = float(input())
    area = first_side * second_side
elif type_of_shape == "circle":
    radius = float(input())
    area = pi * (radius ** 2)
else:
    height = float(input())
    length = float(input())
    area = height * length / 2

print(f"{area:.3f}")