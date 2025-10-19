def characters_in_range(chr1, chr2):
    characters = []
    for current_character in range(ord(chr1) + 1, ord(chr2)):
        characters.append(chr(current_character))
    return characters


first_character = input()
second_character = input()

result = characters_in_range(first_character, second_character)

print(" ".join(result))