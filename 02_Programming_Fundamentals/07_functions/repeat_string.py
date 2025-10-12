some_string = input()
count = int(input())

new_string = lambda a, b: a * b
result = new_string(some_string, count)
print(result)