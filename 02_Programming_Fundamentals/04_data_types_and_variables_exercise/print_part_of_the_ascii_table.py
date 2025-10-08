char_index_start = int(input())
char_index_end = int(input())

for number in range(char_index_start, char_index_end + 1):
    character = chr(number)
    print(character, end=" ")