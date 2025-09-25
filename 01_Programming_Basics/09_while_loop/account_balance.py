money = input()

sum_money = 0

while money != "NoMoreMoney":
    float_money = float(money)

    if float_money < 0:
        print("Invalid operation!")
        break

    else:  # this else is not mandatory, the program can work without it too
        sum_money += float_money
        print(f"Increase: {float_money:.2f}")

    money = input()

print(f"Total: {sum_money:.2f}")