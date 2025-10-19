def sum_of_even(number):
    even_sum = 0
    for current_number in given_number:
        if int(current_number) % 2 == 0:
            even_sum += int(current_number)

    return even_sum


def sum_of_odd(number):
    odd_sum = 0
    for current_number in given_number:
        if int(current_number) % 2 != 0:
            odd_sum += int(current_number)

    return odd_sum


given_number = input()
print(f"Odd sum = {sum_of_odd(given_number)}, Even sum = {sum_of_even(given_number)}")