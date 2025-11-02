first_input = input().split(", ")
second_input = input().split(", ")
print([first_string for first_string in first_input if any(first_string in second_string for second_string in second_input)])