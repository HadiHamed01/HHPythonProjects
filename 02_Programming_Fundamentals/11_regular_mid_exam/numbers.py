numbers = input().split()
my_list = [int(number) for number in numbers]

while True:
    command = input().split()

    if command[0] == "Finish":
        break

    elif command[0] == "Add":
        my_list.append(int(command[1]))

    elif command[0] == "Remove":
        value = int(command[1])
        if value in my_list:
            my_list.remove(value)

    elif command[0] == "Replace":
        value = int(command[1])
        replace = int(command[2])
        if value in my_list:
            index = my_list.index(value)
            my_list[index] = replace

    elif command[0] == "Collapse":
        value = int(command[1])
        my_list = [x for x in my_list if x >= value]

print(" ".join(map(str, my_list)))