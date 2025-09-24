import sys

num_inputs = int(input())

max_input = -sys.maxsize
sum_inputs = 0

for numbers in range(num_inputs):
    user_inputs = int(input())
    sum_inputs += user_inputs
    if user_inputs > max_input:
        max_input = user_inputs

final_sum = sum_inputs - max_input

if max_input == final_sum:
    print(f"Yes \nSum = {final_sum}")
else:
    difference = abs(max_input - final_sum)
    print(f"No \nDiff = {difference}")