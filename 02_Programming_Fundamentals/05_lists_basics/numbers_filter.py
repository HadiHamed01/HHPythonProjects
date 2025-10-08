count = int(input())
my_list = []

for number in range(count):
    value = int(input())
    my_list.append(value)

command = input()

filtered_list = []

if command == "even":
    for current_number in my_list:
        if current_number % 2 == 0:
            filtered_list.append(current_number)

elif command == "odd":
    for current_number in my_list:
        if current_number % 2 != 0:
            filtered_list.append(current_number)

elif command == "negative":
    for current_number in my_list:
        if current_number < 0:
            filtered_list.append(current_number)

elif command == "positive":
    for current_number in my_list:
        if current_number >= 0:
            filtered_list.append(current_number)

print(filtered_list)