def positive_number(list_of_numbers):
    return ', '.join([number for number in list_of_numbers if int(number) >= 0])


def negative_number(list_of_numbers):
    return ', '.join([number for number in list_of_numbers if int(number) < 0])


def even_number(list_of_numbers):
    return ', '.join([number for number in list_of_numbers if int(number) % 2 == 0])


def odd_number(list_of_numbers):
    return ', '.join([number for number in list_of_numbers if int(number) % 2 != 0])


numbers = input().split(", ")
print(f"Positive: {positive_number(numbers)}")
print(f"Negative: {negative_number(numbers)}")
print(f"Even: {even_number(numbers)}")
print(f"Odd: {odd_number(numbers)}")