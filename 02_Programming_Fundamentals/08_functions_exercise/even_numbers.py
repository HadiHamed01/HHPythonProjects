numbers = input().split()
numbers_as_digits = []

for number in numbers:
    numbers_as_digits.append(int(number))

even_numbers = lambda x: x % 2 == 0
filtered_numbers = list(filter(even_numbers, numbers_as_digits))
print(filtered_numbers)