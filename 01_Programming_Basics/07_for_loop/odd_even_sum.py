num_inputs = int(input())

even_sum = 0
odd_sum = 0

for numbers in range(1, num_inputs + 1):
    user_inputs = int(input())
    if numbers % 2 == 0:
        even_sum += user_inputs
    else:
        odd_sum += user_inputs

if even_sum == odd_sum:
    print(f"Yes \nSum = {even_sum}")
else:
    difference = abs(even_sum - odd_sum)
    print(f"No \nDiff = {difference}")