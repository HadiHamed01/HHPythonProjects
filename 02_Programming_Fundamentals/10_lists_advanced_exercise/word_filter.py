some_string = input().split()
filtered_words = [word for word in some_string if len(word) % 2 == 0]
print("\n".join(filtered_words))