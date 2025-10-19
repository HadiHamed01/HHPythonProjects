def perfect_num(number):
    sum_num = 0
    for i in range(1, number):
        if number % i == 0:
            sum_num += i
    if sum_num == value:
        return "We have a perfect number!"
    return "It's not so perfect."


value = int(input())
print(perfect_num(value))