numbers = input().split()
numbers_as_digits = []

for number in numbers:
    numbers_as_digits.append(int(number))

sorted_numbers = sorted(numbers_as_digits)
print(sorted_numbers)