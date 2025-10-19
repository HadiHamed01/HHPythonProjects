def palindrome(numbers):
    if numbers == numbers[::-1]:
        return True
    return False


numbers_as_list = input().split(", ")

for value in numbers_as_list:
    print(palindrome(value))