coffee_price = 1.50
water_price = 1.00
coke_price = 1.40
snacks_price = 2.00

product = input()
amount = int(input())

def total_price(product, amount):
    if product == "coffee":
        return f"{(coffee_price * amount):.2f}"
    elif product == "water":
        return f"{(water_price * amount):.2f}"
    elif product == "coke":
        return f"{(coke_price * amount):.2f}"
    elif product == "snacks":
        return f"{(snacks_price * amount):.2f}"

print(total_price(product, amount))