def add_and_subtract(first_addition, second_addition, subtraction):
    def sum_numbers(first, second):
        return first + second

    def subtract(number):
        return (first_addition + second_addition) - subtraction

    return subtract(subtraction)


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(add_and_subtract(num1, num2, num3))