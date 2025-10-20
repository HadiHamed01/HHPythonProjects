string = input().split()
palindrome_string = input()
my_list = []
palindrome_count = 0

for word in string:
    if word == word[::-1]:
        my_list.append(word)

    if word == palindrome_string:
        palindrome_count += 1

print(f"{my_list} \nFound palindrome {palindrome_count} times")