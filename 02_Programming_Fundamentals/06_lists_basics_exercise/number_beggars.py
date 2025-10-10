money_as_string = input().split(", ")
count_of_beggars = int(input())
money_as_list = []

for number in money_as_string:
    money_as_list.append(int(number))

final_sum_list = []
start_index = 0

for beggar in range(count_of_beggars):
    sum_of_money = 0
    for current_index in range(start_index, len(money_as_list), count_of_beggars):
        sum_of_money += money_as_list[current_index]
    final_sum_list.append(sum_of_money)
    start_index += 1

print(final_sum_list)