K = int(input())
L = int(input())
M = int(input())
N = int(input())

count = 0

for first_digit1 in range(K, 8+1):
    for second_digit1 in range(9, L - 1, -1):
        for first_digit2 in range(M, 8+1):
            for second_digit2 in range(9, N - 1, -1):
                if first_digit1 % 2 == 0 and second_digit1 % 2 != 0 and first_digit2 % 2 == 0 and second_digit2 % 2 != 0:
                    if first_digit1 != first_digit2 or second_digit1 != second_digit2:
                        print(f"{first_digit1}{second_digit1} - {first_digit2}{second_digit2}")
                        count += 1
                        if count == 6:
                            break
                    else:
                        print(f"Cannot change the same player.")

            if count == 6:
                break
        if count == 6:
            break
    if count == 6:
        break