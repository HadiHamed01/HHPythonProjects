number = int(input())

for num in range(1111, 10000):
    is_special = True
    num_as_string = str(num)
    for _ , digit in enumerate(num_as_string):
        current_digit = int(digit)
        if current_digit == 0:
            is_special = False
            break

        if not number % current_digit == 0:
            is_special = False
            break
    if is_special:
        print(f"{num}", end=" ")