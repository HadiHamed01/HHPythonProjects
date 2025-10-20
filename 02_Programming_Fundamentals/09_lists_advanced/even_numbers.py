numbers_list = list(map(int, input().split(", ")))
new_list = [index for index, num in enumerate(numbers_list) if num % 2 == 0]

print(new_list)