number = int(input())

for char1 in range(number):
    for char2 in range(number):
        for char3 in range(number):
            print(f"{chr(97 + char1) + chr(97 + char2) + chr(97 + char3)}")