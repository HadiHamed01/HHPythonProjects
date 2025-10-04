divisor = int(input())
boundary = int(input())
num = boundary

while num % divisor != 0:
    num -= 1

print(num)