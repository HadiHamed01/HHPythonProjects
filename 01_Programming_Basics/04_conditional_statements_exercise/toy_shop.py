puzzle_price = 2.60
doll_price = 3
bear_price = 4.10
minion_price = 8.20
truck_price = 2

vacation_price = float(input())
amount_puzzles = int(input())
amount_dolls = int(input())
amount_bears = int(input())
amount_minions = int(input())
amount_trucks = int(input())

total_amount_of_toys = amount_puzzles + amount_dolls + amount_bears + amount_minions + amount_trucks
total_price_of_toys = (amount_puzzles * 2.60) + (amount_dolls * 3) + (amount_bears * 4.10) \
    + (amount_minions * 8.20) + (amount_trucks * 2)

discounted_price = 0

if total_amount_of_toys >= 50:
    discount = 0.25
    discounted_price = total_price_of_toys * discount

profit_after_discount = total_price_of_toys - discounted_price
rent = profit_after_discount * 0.1
profit_after_rent = profit_after_discount - rent

if profit_after_rent >= vacation_price:
    leftover_money = profit_after_rent - vacation_price
    print(f"Yes! {leftover_money:.2f} lv left.")
else:
    needed_money = vacation_price - profit_after_rent
    print(f"Not enough money! {needed_money:.2f} lv needed.")