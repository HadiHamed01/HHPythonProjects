import sys

number = input()

max_number = - sys.maxsize

while number != "Stop":
    integer_number = int(number)

    if integer_number > max_number:
        max_number = integer_number

    number = input()

print(max_number)