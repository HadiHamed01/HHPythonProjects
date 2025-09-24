age = int(input())
laundry_machine_price = float(input())
price_per_toy = int(input())

money = 0
toys = 0
money_lost = 0
money_sum = 0

for birthday in range(1, age + 1):

    if birthday % 2 == 0:
        money += 10
        money_sum += money
        money_lost += 1

    else:
        toys += 1

total_price_per_toy = price_per_toy * toys
total_money = money_sum - money_lost
final_money = total_money + total_price_per_toy

if final_money >= laundry_machine_price:
    print(f"Yes! {(final_money - laundry_machine_price):.2f}")
else:
    print(f"No! {(laundry_machine_price - final_money):.2f}")