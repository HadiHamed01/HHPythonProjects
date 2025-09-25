change_amount = float(input())

change_amount_as_pennies = int(change_amount * 100)   # 2,23 => 233 pennies
# [2lv = 200st, 1lv = 100, 50st, 20st, 10st, 5st, 2st, 1st]

coins_count = 0

while change_amount_as_pennies > 0:
    if change_amount_as_pennies >= 200:
        change_amount_as_pennies -= 200
    elif change_amount_as_pennies >= 100:
        change_amount_as_pennies -= 100
    elif change_amount_as_pennies >= 50:
        change_amount_as_pennies -= 50
    elif change_amount_as_pennies >= 20:
        change_amount_as_pennies -= 20
    elif change_amount_as_pennies >= 10:
        change_amount_as_pennies -= 10
    elif change_amount_as_pennies >= 5:
        change_amount_as_pennies -= 5
    elif change_amount_as_pennies >= 2:
        change_amount_as_pennies -= 2
    elif change_amount_as_pennies >= 1:
        change_amount_as_pennies -= 1

    coins_count += 1

print(coins_count)