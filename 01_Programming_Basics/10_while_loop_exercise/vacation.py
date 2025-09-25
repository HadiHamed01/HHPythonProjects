vacation_cost = float(input())
starting_money = float(input())

sum_of_money = starting_money
total_days = 0
consecutive_days_spending_money = 0

while True:
    action = input()
    amount_based_on_action = float(input())
    total_days += 1

    if action == "spend":
        consecutive_days_spending_money += 1
        sum_of_money -= amount_based_on_action

        if sum_of_money < 0:
            sum_of_money = 0

        if consecutive_days_spending_money >= 5:
            break

    elif action == "save":
        consecutive_days_spending_money = 0
        sum_of_money += amount_based_on_action

        if sum_of_money >= vacation_cost:
            break

if sum_of_money >= vacation_cost:
    print(f"You saved the money for {total_days} days.")
else:
    print(f"You can't save the money.\n{total_days}")