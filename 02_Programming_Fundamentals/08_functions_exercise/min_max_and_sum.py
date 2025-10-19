numbers = input().split()
numbers_as_digits = []

for number in numbers:
    numbers_as_digits.append(int(number))

min_num = min(numbers_as_digits)
max_num = max(numbers_as_digits)
sum_num = sum(numbers_as_digits)

print(f"The minimum number is {min_num} \nThe maximum number is {max_num} \nThe sum number is: {sum_num}")