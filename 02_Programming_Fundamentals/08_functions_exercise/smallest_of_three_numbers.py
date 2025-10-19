def smallest_number(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(smallest_number(num1, num2, num3))