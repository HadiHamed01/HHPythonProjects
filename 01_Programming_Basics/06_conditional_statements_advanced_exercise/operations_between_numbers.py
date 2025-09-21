first_number = int(input())
second_number = int(input())
symbol = str(input())

sum = 0
even_or_odd = ""

if symbol == "+":
    sum = first_number + second_number
    if sum % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{first_number} {symbol} {second_number} = {sum} - {even_or_odd}")

elif symbol == "-":
    sum = first_number - second_number
    if sum % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{first_number} {symbol} {second_number} = {sum} - {even_or_odd}")

elif symbol == "*":
    sum = first_number * second_number
    if sum % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{first_number} {symbol} {second_number} = {sum} - {even_or_odd}")

elif symbol == "/":
    if second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        sum = first_number / second_number
        print(f"{first_number} / {second_number} = {sum:.2f}")

elif symbol == "%":
    if second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        sum = first_number % second_number
        print(f"{first_number} % {second_number} = {sum}")