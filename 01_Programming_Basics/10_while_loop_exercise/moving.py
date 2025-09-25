width = int(input())
length = int(input())
height = int(input())
boxes_count = input()

space_left = width * length * height

while boxes_count != "Done":
    boxes_count = int(boxes_count)
    space_left -= boxes_count

    if space_left < 0:
        print(f"No more free space! You need {abs(space_left)} Cubic meters more.")
        break

    boxes_count = input()

else:
    print(f"{space_left} Cubic meters left.")