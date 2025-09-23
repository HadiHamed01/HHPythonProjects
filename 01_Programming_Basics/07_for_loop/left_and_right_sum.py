num_inputs = int(input())

left_sum = 0
right_sum = 0

for numbers in range(num_inputs * 2):
    user_inputs = int(input())
    if numbers < num_inputs:
        left_sum += user_inputs
    else:
        right_sum += user_inputs

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    difference = abs(left_sum - right_sum)
    # we use absolute value because we dont care which is smaller/bigger
    print(f"No, diff = {difference}")