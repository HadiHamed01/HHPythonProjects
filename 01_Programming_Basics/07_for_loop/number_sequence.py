import sys

num_inputs = int(input())

max_number = - sys.maxsize
min_number = sys.maxsize

for numbers in range(num_inputs):
    user_inputs = int(input())
    if user_inputs > max_number:
        max_number = user_inputs
    if user_inputs < min_number:
        min_number = user_inputs

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")