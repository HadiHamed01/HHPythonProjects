total_yards = float(input())
price_for_one_yard = 7.61
discount = 0.18
total_price = price_for_one_yard * total_yards
total_discount = discount * total_price
final_price = total_price - total_discount
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {total_discount} lv.")