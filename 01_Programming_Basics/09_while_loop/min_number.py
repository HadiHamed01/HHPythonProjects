import sys

number = input()

min_number = sys.maxsize

while number != "Stop":
    integer_number = int(number)

    if integer_number < min_number:
        min_number = integer_number

    number = input()

print(min_number)