num = int(input())

for i in range(1, num + 1):
    for y in range(0, i):
        print("*", end="")
    print()

for i in range(num -1, 0, -1):
    for y in range(0, i):
        print("*", end="")
    print()