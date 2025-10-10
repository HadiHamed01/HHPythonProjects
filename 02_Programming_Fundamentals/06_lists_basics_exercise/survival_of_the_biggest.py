given_numbers = input().split()
count_to_remove = int(input())
my_list = []

for value in given_numbers:
    my_list.append(int(value))

for number in range(count_to_remove):
    min_num = min(my_list)
    my_list.remove(min_num)

print(str(my_list)[1:-1]) # [1:-1] is used to remove the square brackets when printing the list