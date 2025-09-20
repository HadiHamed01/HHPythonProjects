budget = float(input())
videocard_count = int(input())
processor_count = int(input())
ram_count = int(input())

videocard_price = 250
videocard_price_sum = videocard_count * videocard_price

processor_price = videocard_price_sum * 0.35
processor_price_sum = processor_count * processor_price

ram_price = videocard_price_sum * 0.1
ram_price_sum = ram_count * ram_price

total_price = videocard_price_sum + processor_price_sum + ram_price_sum

if videocard_count > processor_count:
    discount = 0.15
    total_price = total_price - (total_price * 0.15)

leftover_money = budget - total_price

if budget >= total_price:
    print(f"You have {leftover_money:.2f} leva left!")
else:
    print(f"Not enough money! You need {-leftover_money:.2f} leva more!")