count = int(input())
word = input()
my_list = []

for number in range(count):
    some_string = input()
    my_list.append(some_string)

print(my_list)

filtered_list = []

for current_string in my_list:
    if word in current_string:
        filtered_list.append(current_string)

print(filtered_list)